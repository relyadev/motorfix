from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class Client(AbstractUser):
    username = None
    phone_number = models.IntegerField()
    email = models.EmailField(_("email addres"), unique=True)
    points_count = models.IntegerField(default=0)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email

class Car(models.Model):
    brand = models.CharField(max_length=100)
    mileage = models.IntegerField()
    VIN = models.CharField(max_length=17, unique=True)
    year_of_issue = models.IntegerField()
    image_car = models.ImageField(default=None, null=True)
    user = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.brand} | {self.VIN}"

class CarHistory(models.Model):
    class StatusRepair(models.TextChoices):
        START = "Обработка", _("В обработке")
        PROGRESS = "Выполняется", _("В ремонте")
        FINISH = "Готово", _("Готово к выдаче")
        CLOSE = "Выдан", _("Завершено")

    date_of_repair = models.DateField(default=datetime.now())
    description_repair = models.TextField(default=None)
    status = models.CharField(max_length=100, default=StatusRepair.START, choices=StatusRepair.choices)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.car.brand if self.car else "Машина не существует" } | {self.status} | {self.date_of_repair}"