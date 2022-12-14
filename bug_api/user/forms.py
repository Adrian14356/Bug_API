from django.contrib.auth.forms import UserCreationForm, User
from django import forms
from .models import User


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]