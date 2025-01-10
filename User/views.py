from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import CustomUserChangeForm
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import MotoristSignupForm, LoginForm, CustomUserChangeForm
from django.contrib import messages # For Admin error message
from django.utils.safestring import mark_safe # For Admin error message
from django.urls import reverse  # For Admin error message
from tickets.models import Ticket
# from .models import Motorist
# from django.contrib.auth.decorators import login_required


# Home page view
def home(request):
    return render(request, 'home.html')


# Motorist signup view
def motorist_signup(request):
    if request.method == 'POST':
        form = MotoristSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('motorist-login')
        else:
            messages.error(request, 'An error occurred. Please try again.')
            return render(request, 'motorist-signup.html', {'form': form})
    else:
        form = MotoristSignupForm()

    return render(request, 'motorist-signup.html', {'form': form})


# Motorist login view
def motorist_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate (request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard-motorist')  # Redirect to the home page or dashboard
            else:
                form.add_error(None, "Invalid username or password.")
        else:
            print(form.errors)  # For debugging purposes
    else:
        form = LoginForm()
    return render(request, 'motorist-login.html', {'form': form})


# Official login view
def official_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate (request, username=username, password=password)
            if user is not None:
                if user.is_staff:  # Check if the user is an official
                    login(request, user)
                    return redirect('dashboard-official')  # Redirect to the home page or dashboard
                
                else:
                    motorist_login_url = reverse('motorist-login')
                    # If the user is not an admin, show an error message and redirect to motorist login
                    message = mark_safe(
                        f'You are not an Official. Please log in as an Motorist. <a href="{motorist_login_url}">Click here</a> to go to the motorist login page.'
                    )
                    messages.error(request, message)
                    # return redirect('motorist_login')  # Redirect to the official login page

            else:
                form.add_error(None, "Invalid username or password.")
        else:
            print(form.errors)  # For debugging purposes
    else:
        form = LoginForm()
    return render(request, 'official-login.html', {'form': form})


# Admin login view
def admin_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate (request, username=username, password=password)
            if user is not None:
                if user.is_superuser:  # Check if the user is an admin
                    login(request, user)
                    return redirect('dashboard-admin')  # Redirect to the admin dashboard
                
                elif user.is_staff:  # Check if the user is an official
                    official_login_url = reverse('official-login')
                    # If the user is not an admin, show an error message and redirect to official login
                    message = mark_safe(
                        f'You are not an admin. Please log in as an Official. <a href="{official_login_url}">Click here</a> to go to the official login page.'
                    )
                    messages.error(request, message)
                    # return redirect('official_login')  # Redirect to the official login page
                
                else:

                    motorist_login_url = reverse('motorist-login')
                    # If the user is not an admin, show an error message and redirect to motorist login
                    message = mark_safe(
                        f'You are not an admin. Please log in as an Motorist. <a href="{motorist_login_url}">Click here</a> to go to the motorist login page.'
                    )
                    messages.error(request, message)
                    # return redirect('motorist_login')  # Redirect to the official login page
            else:
                form.add_error(None, "Invalid username or password.")
        else:
            print(form.errors)  # For debugging purposes
    else:
        form = LoginForm()

    return render(request, 'admin-login.html', {'form': form})
                
        
# Motorist dashboard view
def dashboard_motorist(request):
    tickets = Ticket.objects.select_related('offence').filter(motorist=request.user)
    return render(request, 'dashboard-motorist.html', {'tickets': tickets})


# Official dashboard view
def dashboard_official(request):
    tickets = Ticket.objects.select_related('offence').filter(official=request.user)
    return render(request, 'dashboard-official.html', {'tickets': tickets})


# Admin dashboard view
def dashboard_admin(request):
    tickets = Ticket.objects.select_related('offence').filter(motorist=request.user)
    return render(request, 'dashboard-admin.html', {'tickets': tickets})



def motorist_profile(request):
    motorist = request.user # Get the current user 

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            print('Profile updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
            print(form.errors)

    else:
        form = CustomUserChangeForm(instance=request.user)

    context = {
        'form': form,
        'date_joined': motorist.date_joined,
        'last_login': motorist.last_login,
    }

    return render(request, 'profile.html', context)


def m_ticket_history(request):
    tickets = Ticket.objects.select_related('offence').filter(motorist=request.user)
    return render (request, 'm_ticket-history.html', {'tickets': tickets})
    
def o_ticket_history(request):
    tickets = Ticket.objects.select_related('offence').filter(official=request.user)
    return render (request, 'o_ticket-history.html', {'tickets': tickets})


# Logout view
def logout_user(request):
    logout(request)
    return redirect('home')


# Redirect to the admin login page
def admin_login_redirect(request):
    return redirect(reverse('admin:login'))