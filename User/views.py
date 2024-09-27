from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Motorist 
from .forms import MotoristSignupForm

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

def motorist_login(request):
    return render(request, 'motorist_login.html')

def admin_login_redirect(request):
    return redirect(reverse('admin:login'))