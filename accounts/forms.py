from django import forms
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    """ This class will represent the login form """

    username = forms.CharField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    """ This class will represent the registration Forms """

    username = forms.CharField(widget=forms.TextInput)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)