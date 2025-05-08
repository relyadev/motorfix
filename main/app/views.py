from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from app.forms import RegistrationForm
from django.contrib.auth.views import LoginView
from app.forms import LoginForm
from app.models import Car, Client, CarHistory
from django.contrib.auth.decorators import login_required
from app.forms import AddCarForm, AddOrderForm
from django.core.files.storage import FileSystemStorage

class EmailLogin(LoginView):
    form_class = LoginForm
    template_name = "registration/login.html"

def registration(req: HttpRequest):
    if req.method == "POST":
        form = RegistrationForm(req.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data.get("password"))
            user.save()
            return redirect("login")
        
    form = RegistrationForm()
    return render(req, 'registration/registration.html', {"form": form})

@login_required
def main(req: HttpRequest):
    return render(req, "index.html")

@login_required

def garage(req: HttpRequest):
    user = req.user
    cars = Car.objects.filter(user__id = user.id).all()
    add_car_form = AddCarForm()
    return render(req, "garage.html", {"cars": cars, "form": add_car_form})

@login_required

def history(req: HttpRequest):
    user = req.user
    orders = CarHistory.objects.filter(car__user =user).all()
    return render(req, "history.html", {"orders": orders})

@login_required
def order(req: HttpRequest):
    # user = req.user
    add_order_form = AddOrderForm(user = req.user)
    # cars = Car.objects.filter(user__id = user.id).all()
    return render(req, "order.html", {"form": add_order_form})

@login_required
def add_car(req: HttpRequest):
    if req.method == "POST":
        # (brand, mileage, VIN, year_of_issue, image_car) = (
        # req.POST.get("brand"), req.POST.get("mileage"), req.POST.get("VIN"), 
        # req.POST.get("year_of_issue"), req.POST.get("image_car")
        # )
        # if 'image_car' in req.FILES:
        #     image_car = req.FILES['image_car']
        #     fs = FileSystemStorage()
        #     file_name = fs.save(image_car.name, image_car)
        #     file_url = fs.url(file_name)

        form = AddCarForm(req.POST, req.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = req.user
            car.save()


        # Car.objects.create(brand=brand, mileage=mileage, VIN=VIN, year_of_issue=year_of_issue, image_car=file_url, user_id=req.user.id)
    return redirect("garage")

@login_required
def make_order(req: HttpRequest):
    form = AddOrderForm(req.POST, user = req.user)
    if form.is_valid():
        car = form.save(commit=False)
        car.user = req.user
        car.save()
    return redirect("history")