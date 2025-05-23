from django import forms
from .models import Car, Client, CarHistory
from django.contrib.auth.forms import AuthenticationForm

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confrim = forms.CharField(
        widget = forms.PasswordInput, 
        label = "Confrim password")
    class Meta:
        model = Client
        fields = ["first_name", "last_name", "email", "password", "phone_number"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confrim = cleaned_data.get("password_confrim")

        if password != password_confrim:
            raise forms.ValidationError("Пароли не совпадают!")
        email = cleaned_data.get("email")
        if Client.objects.filter(email=email).exists():
            raise forms.ValidationError("Это email уже существует")
        return cleaned_data
    

class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(), label="Email")

class AddCarForm(forms.ModelForm):
    # brand = forms.CharField(label="Марка")
    # mileage = forms.IntegerField(label="Пробег")
    # VIN = forms.CharField(label="VIN номер")
    # year_of_issue = forms.IntegerField(label="Год выпуска")
    # image_car = forms.ImageField(label="Изображение")

    class Meta:
        model = Car
        fields = ["brand",
            "mileage",
            "VIN",
            "year_of_issue",
            "image_car"
        ]

class AddOrderForm(forms.ModelForm):
    class Meta:
        model = CarHistory
        fields = ["car", "description_repair"]
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['car'].queryset = Car.objects.filter(user=user)