from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Motorist 
from .forms import MotoristSignupForm, LoginForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def motorist_signup(request):
    if request.method == 'POST':
        form = MotoristSignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('motorist_login')
    else:
        form = MotoristSignupForm()

    return render(request, 'motorist_signup.html', {'form': form})

# def motorist_login(request):
#     return render(request, 'motorist_login.html')

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate (request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to the home page or dashboard
            else:
                form.add_error(None, "Invalid username or password.")
        else:
            print(form.errors)  # For debugging purposes
    else:
        form = LoginForm()
    return render(request, 'motorist_login.html', {'form': form})
        

def dashboard(request):
    return render(request, 'dashboard_motorist.html')

def logout(request):
    return redirect('home')

def admin_login_redirect(request):
    return redirect(reverse('admin:login'))