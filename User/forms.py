from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Motorist

class MotoristSignupForm(forms.ModelForm):
    class Meta:
        model = Motorist
        fields = ('first_name', 'last_name', 'email', 'license_no')