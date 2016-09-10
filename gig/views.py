from django.shortcuts import render

# Create your views here.
from django import template

def homeView(request):
    return render(request, 'base.html')
