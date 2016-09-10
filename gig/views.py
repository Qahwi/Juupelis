from django.shortcuts import render
from django.contrib.auth import authenticate, login
from forms import *


# Create your views here.
from django import template

def HomeView(request):
    return render(request, 'base.html')

def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home/')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
