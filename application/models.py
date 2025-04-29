from django.db import models
from datetime import date

# Create your models here.
# create table here , register in admin page , run makemigrations and migrate command
# write the data storing code in views.py , display appropriate message in above the form after submission 


class contact_table(models.Model):
    name = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    enquiry = models.CharField(max_length=30)
    message =models.TextField()
    contacted = models.BooleanField(default=False)
    submitdate = models.DateField(default=date.today)


    def __str__(self):
        return self.name
    
class book_table(models.Model):
    submitdate = models.DateField(default=date.today)  # Correct default
    name = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    date = models.DateField()
    time = models.TimeField()
    people = models.PositiveIntegerField()
    message =models.TextField()
    contacted = models.BooleanField(default=False)
    reservation = models.CharField(max_length=100, default="Confirmed")  

    def __str__(self):
        return self.name
    

class event_table(models.Model):
    submitdate = models.DateField(default=date.today)  # Correct default
    name = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    date = models.DateField()
    time = models.TimeField()
    people = models.PositiveIntegerField()
    eventname = models.CharField(max_length=50,default='Other')
    message =models.TextField()
    contacted = models.BooleanField(default=False)
    reservation = models.CharField(max_length=100, default="Confirmed")  


    def __str__(self):
        return self.name
    
