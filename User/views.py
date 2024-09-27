from django.contrib.auth import authenticate, login
#from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Motorist 
from .forms import MotoristSignupForm, MotoristLoginForm

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

def motorist_login(request):
    if request.method == 'POST':
        form = MotoristLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            license_no = form.cleaned_data['license_no']
            try:
                user = Motorist.objects.get(email=email, license_no=license_no)
                login(request, user)  # Use Django's login method
                return redirect('dashboard_motorist')  # Redirect to the motorist dashboard
            except Motorist.DoesNotExist:
                form.add_error(None, 'Invalid email or license number')
    else:
        form = MotoristLoginForm()
    return render(request, 'motorist_login.html', {'form': form})


def dashboard_motorist(request):
    return render(request, 'dashboard_motorist.html')

def admin_login_redirect(request):
    return redirect(reverse('admin:login'))