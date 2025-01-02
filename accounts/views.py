from django.shortcuts import render, redirect
from .forms import MotoristSignupForm, MotoristLoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def motorist_login(request):
    if request.method == 'POST':
        form = MotoristLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            license_no = form.cleaned_data['license_no']

            user = authenticate(request, username=email, license_no=license_no)
            print(f"Authenticated user: {user}")

            if user is not None:
                login(request, user)
                print(f"Session data: {request.session.items()}")

                next_url = request.GET.get('next', None)
                if next_url:
                    print(f"Redirecting to next: {next_url}")
                else:
                    print(f"No next parameter found, redirecting to dashboard_motorist")

                # If there's no next URL, default to 'dashboard_motorist'
                return redirect(next_url if next_url else 'dashboard_motorist')

                # next_url = request.GET.get('next', 'dashboard_motorist')
                # return redirect(next_url)

                # return redirect('dashboard_motorist')
            
            else:
                form.add_error(None, "Invalid email or license number.")
        else:
            form = MotoristLoginForm()

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

@login_required
def dashboard_motorist(request):
    print(f"Logged in user: {request.user}")  # Debugging
    return render(request, 'dashboard_motorist.html')

# def motorist_signup(request):
#     return render(request, 'motorist_signup.html')