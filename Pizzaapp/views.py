from django.shortcuts import render, redirect, HttpResponseRedirect,HttpResponse
from Pizzaapp.models import Member #models.py
from Pizzaapp.models import EmployeeDetails
from Pizzaapp.models import TableBook
from Pizzaapp.forms import TableBookForm
from Pizzaapp.models import OrderPizza
from Pizzaapp.forms import OrderPizzaForm
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        member = Member(username=request.POST['username'], password=request.POST['password'],  firstname=request.POST['firstname'], lastname=request.POST['lastname'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'Pizzaapp/index.html')
 
def login(request):
    return render(request, 'Pizzaapp/login.html')
 
def home(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'Pizzaapp/home.html', {'member': member})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'Pizzaapp/login.html', context)
def home(request):
    return render(request,'Pizzaapp/home.html')

def about(request):
    return render(request,'Pizzaapp/about-us.html')
def contact(request):
    data=EmployeeDetails.objects.all()
    return render(request,'Pizzaapp/contact-Us.html',context={"data":data})
def gallery(request):
    return render(request,'Pizzaapp/gallery.html')

def booktable(request):
    if request.method=='POST':
        form=TableBookForm(request.POST)
        if form.is_valid():
            form.save()
        form=TableBookForm()
        messages.success(request,"Your Have Bookedtable Sucessfully")
        return render(request,'Pizzaapp/booktable.html',context={"form":form})
    return render(request,'Pizzaapp/booktable.html')

def orderpizza(request):
    if request.method == 'POST':
        data=OrderPizza(name=request.POST['name'],contactno=request.POST['contactno'],location=request.POST['location'],pizzatype=request.POST['pizzatype'],platesno=request.POST['platesno'])
        data.save()
        data=OrderPizza.objects.all()
        messages.success(request,"Your Order Send Sucessfully")
    return render(request,'Pizzaapp/order.html')