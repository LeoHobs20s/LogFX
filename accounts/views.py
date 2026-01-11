from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import LoginForm, RegistrationForm


def login_view(request):
    """ This view will render the login feature for the web app """

    if request.method != 'POST':
        # No Data Submitted; create blank form
        form = LoginForm()
    else:
        # POST Data Submitted; process data
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    
    context = {'form':form}
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    """ This view will render the logout feature """

    logout(request)
    return HttpResponseRedirect(reverse('login_view'))


def register(request):
    """ This view will render the registration form """

    if request.method != 'POST':
        # No Data Submitted; create blank form
        form = RegistrationForm()
    else:
        # POST Data Submitted; process data
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            user = authenticate(username=new_user.username, password=request.POST['password1'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    
    return render(request, 'accounts/register.html', {'form':form})