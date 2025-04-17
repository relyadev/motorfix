from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Car(models.Model):
    brand = models.CharField(max_length=100)
    mileage = models.IntegerField()
    VIN = models.CharField(max_length=17)
    year_of_issue = models.IntegerField()
    image_car = models.ImageField(upload_to="uploads/")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class CarHistory(models.Model):
    date_of_repair = models.DateField()
    name_repair = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)

class Client(AbstractUser):
    phone_number = models.IntegerField(max_length=11)

