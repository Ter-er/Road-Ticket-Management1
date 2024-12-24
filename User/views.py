from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Motorist 
from .forms import MotoristSignupForm, LoginForm
from django.contrib import messages # For Admin error message
from django.utils.safestring import mark_safe # For Admin error message
from django.urls import reverse  # For Admin error message


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

# def login_user(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate (request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('dashboard')  # Redirect to the home page or dashboard
#             else:
#                 form.add_error(None, "Invalid username or password.")
#         else:
#             print(form.errors)  # For debugging purposes
#     else:
#         form = LoginForm()
#     return render(request, 'motorist_login.html', {'form': form})



def official_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate (request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard_official')  # Redirect to the home page or dashboard
            else:
                form.add_error(None, "Invalid username or password.")
        else:
            print(form.errors)  # For debugging purposes
    else:
        form = LoginForm()
    return render(request, 'official_login.html', {'form': form})



def admin_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate (request, username=username, password=password)
            if user is not None:
                if user.is_staff:  # Check if the user is an admin
                    login(request, user)
                    return redirect('dashboard_admin')  # Redirect to the admin dashboard
                else:

                    official_login_url = reverse('official_login')
                    # If the user is not an admin, show an error message and redirect to official login
                    message = mark_safe(
                        f'You are not an admin. Please log in as an official. <a href="{official_login_url}">Click here</a> to go to the official login page.'
                    )
                    messages.error(request, message)
                    # return redirect('official_login')  # Redirect to the official login page
            else:
                form.add_error(None, "Invalid username or password.")
        else:
            print(form.errors)  # For debugging purposes
    else:
        form = LoginForm()

    return render(request, 'admin_login.html', {'form': form})
                
        

def dashboard(request):
    return render(request, 'dashboard_motorist.html')



def dashboard_official(request):
    return render(request, 'dashboard_official.html')



def dashboard_admin(request):
    return render(request, 'dashboard_admin.html')



def logout_user(request):
    logout(request)
    return redirect('home')



def admin_login_redirect(request):
    return redirect(reverse('admin:login'))