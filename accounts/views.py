from django.shortcuts import render, redirect
from .forms import MotoristSignupForm

# Create your views here.

def motorist_login(request):
    return render(request, 'motorist_login.html')


def motorist_signup(request):
    if request.method == 'POST':
        form = MotoristSignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('motorist_login')
    else:
        form = MotoristSignupForm()

    return render(request, 'motorist_signup.html', {'form': form})


# def motorist_signup(request):
#     return render(request, 'motorist_signup.html')