from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from app.forms import RegistrationForm
from django.contrib.auth.views import LoginView
from app.forms import LoginForm
from app.models import Car, CarHistory
from django.contrib.auth.decorators import login_required
from app.forms import AddCarForm, AddOrderForm, UpdateCarForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_email(template_name, context, subject, user):
    html_content = render_to_string(
        f"emails/{template_name}",
        context = context,
    )
    text_content = strip_tags(html_content)
    
    msg = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email="relyadev@gmail.com",
        to=[user.email]
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    
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
def add_car(req: HttpRequest):
    if req.method == "POST":
        form = AddCarForm(req.POST, req.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = req.user
            car.save()
    return redirect("garage")

@login_required
def delete_car(req: HttpRequest, id):
    if req.method == "POST":
        user = req.user
        Car.objects.filter(id=id, user=user).get().delete()
    return redirect("garage")

@login_required
def update_car(req: HttpRequest, id):
    user = req.user
    car = get_object_or_404(Car, id=id, user=user)
    if req.method == "POST":
        form = UpdateCarForm(req.POST, instance=car)
        if form.is_valid():
            car = form.save(commit=False)
            car.save()
        return redirect("garage")
    else:
        form = UpdateCarForm(instance=car)
    return render(req, "edit_car.html", {"form": form, "car": car})

@login_required
def history(req: HttpRequest):
    user = req.user
    orders = CarHistory.objects.filter(car__user =user).all()
    return render(req, "history.html", {"orders": orders})

@login_required
def order(req: HttpRequest):
    add_order_form = AddOrderForm(user = req.user)
    return render(req, "order.html", {"form": add_order_form})

@login_required
def make_order(req: HttpRequest):
    form = AddOrderForm(req.POST, user = req.user)
    if form.is_valid():
        car = form.save(commit=False)
        car.user = req.user
        car.save()
    send_email("mail_new_order.html", {"order": car}, "Новая заявка", req.user)
    return redirect("history")