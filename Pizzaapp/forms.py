from django import forms
from Pizzaapp.models import TableBook,OrderPizza

class TableBookForm(forms.ModelForm):
	class Meta:
		model = TableBook
		fields = '__all__'

class OrderPizzaForm(forms.ModelForm):
	class Meta:
		model = OrderPizza
		fields = ('name','contactno','location','pizzatype','platesno')
		widgets={
		'name' : forms.TextInput(attrs={'class':'form-control'}),
		'contactno' : forms.NumberInput(attrs={'class':'form-control'}),
		'location' : forms.TextInput(attrs={'class':'form-control'}),
		'pizzatype' : forms.Select(attrs={'class':'form-control'}),
		'platesno' : forms.Select(attrs={'class':'form-control'}),

		}