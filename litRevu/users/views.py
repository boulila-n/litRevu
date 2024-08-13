from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from . import forms


def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Identifiants invalides.'
    return render(request, 'login.html', context={'form': form,
                                                  'message': message})


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def home(request):
    return redirect('home')


def signup_page(request):
    form = forms.SignupForm()
    message = ''
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            message = 'inscription terminée avec succées !'
    return render(request, 'signup.html', context={'form': form,
                                                   'message': message})
