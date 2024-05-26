from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class RegisterForm(UserCreationForm):
    # firstname = forms.CharField(max_length=100)
    # lastname = forms.CharField(max_length=100)
    email = forms.CharField(
        max_length=255, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = {'username', 'email', 'password1', 'password2'}


class SignUpForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name",
                  "email", "username", "password1", "password2")
