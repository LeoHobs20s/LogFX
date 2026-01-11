from django import forms


class LoginForm(forms.Form):
    """ This class will represent the login form """

    username = forms.CharField(max_length=120)
    password = forms.CharField(widget = forms.PasswordInput)