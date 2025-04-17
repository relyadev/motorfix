from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from app.forms import RegistrationForm

def registration(req: HttpRequest) -> render:
    if req.method == "POST":
        form = RegistrationForm(req.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data.get("password"))
            user.save()
            # send_mail(
            #     "Accert email",
            #     "Hello!",
            #     fail_silently=True,
            #     from_email="mohvardeno@gmail.com",
            #     recipient_list = [user.get("email")]
            # )
            return redirect("login")
    form = RegistrationForm()
    return render(req, 'registration/registration.html', {"form": form})

def main(req: HttpRequest):
    return render(req, "index.html")