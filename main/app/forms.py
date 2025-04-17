from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confrim = forms.CharField(
        widget = forms.PasswordInput, 
        label = "Confrim password")
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confrim = cleaned_data.get("password_confrim")

        if password != password_confrim:
            raise forms.ValidationError("Пароли не совпадают!")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Это email уже существует")
        return cleaned_data