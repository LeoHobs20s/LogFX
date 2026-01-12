from django import forms
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    """ This class will represent the login form """

    username = forms.CharField(max_length=120,widget=forms.TextInput(attrs={'class':'form-control w-50', 'placeholder':'Enter your username'}),
                            help_text='120 Character max.', error_messages={'required':'Enter your username'})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control w-50', 'placeholder':'Enter your password'}), error_messages={'required':'Enter your password'})


class RegistrationForm(UserCreationForm):
    """ This class will represent the registration Forms """

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control w-50', 'placeholder':'Enter a username'}), help_text='120 Characters max', error_messages={'required':'Enter a username'})
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control w-50', 'placeholder':'Enter a password'}), error_messages={'required':'Enter a password'}, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control w-50', 'placeholder':'Confirm Password'}), error_messages={'required':'Enter a password'}, label='Confirm Password')