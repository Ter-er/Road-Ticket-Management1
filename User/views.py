from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Motorist 

# Create your views here.
def home(request):
    return render(request, 'home.html')

def motorist_signup(request):
    return render(request, 'motorist_signup.html')

def motorist_login(request):
    return render(request, 'motorist_login.html')

def admin_login_redirect(request):
    return redirect(reverse('admin:login'))