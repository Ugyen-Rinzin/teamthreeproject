#models.py
from django.db import models
import datetime

GENDER=[
('Male','Male'),
('Femail','Femail'),
('Other', 'Other')
]


PIZZATYPE=[
('vegetarian','vegetarian'),
('Non-vegetarian','Non-vegetarian')
]

PLATESNO=[
(1,1),
(2,2),
(3,3),
(4,4)
]

# Create your models here.
class Member(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=12)
 
    def __str__(self):
        return self.firstname + " " + self.lastname
   
  
    class Meta:  
        db_table = "web_member"

class EmployeeDetails(models.Model):
    empid= models.CharField(unique=True,max_length=50)
    name = models.CharField(max_length=50)
    department = models.CharField( max_length=50)
    gender = models.CharField(choices=GENDER, max_length=50)
    email = models.CharField(max_length=50)
    contact = models.IntegerField()

    class Meta:
        verbose_name='EmployeeDetails'
        verbose_name_plural='EmployeeDetailss'
    def __str__(self):
        return self.empid


class TableBook(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    contactNo = models.CharField(max_length=8)
    date = models.DateTimeField(null=True)
    time = models.TimeField(null=True)
    peopleno = models.IntegerField()
    message = models.TextField()

    class Meta:
        verbose_name='TableBook'
        verbose_name_plural='TableBooks'

    def __str__(self):
        return self.name

class OrderPizza(models.Model):
    name = models.CharField(max_length=50)
    contactno = models.IntegerField()
    location = models.CharField(max_length=90)
    pizzatype = models.CharField(choices=PIZZATYPE, max_length=50)
    platesno = models.IntegerField(choices=PLATESNO,)

    class Meta:
        verbose_name='OrderPizza'
        verbose_name_plural='OrderPizzas'
    def __str__(self):
        return self.name