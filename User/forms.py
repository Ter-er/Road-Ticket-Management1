from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MotoristSignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

    
    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.first_name = (self.cleaned_data['first_name'])
    #     user.last_name = (self.cleaned_data['last_name'])
    #     if commit:
    #         user.save()
    #     return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
