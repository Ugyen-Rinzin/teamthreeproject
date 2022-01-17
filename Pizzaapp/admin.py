from django.contrib import admin
from Pizzaapp.models import Member,EmployeeDetails,TableBook,OrderPizza

# Register your models here.
admin.site.register(Member)
admin.site.register(EmployeeDetails)
admin.site.register(TableBook)
admin.site.register(OrderPizza)
