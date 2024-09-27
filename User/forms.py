from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Motorist

class MotoristSignupForm(forms.ModelForm):
    class Meta:
        model = Motorist
        fields = ('first_name', 'last_name', 'email', 'license_no')


class MotoristLoginForm(forms.Form):
    email = forms.EmailField()
    license_no = forms.CharField(max_length=20)
