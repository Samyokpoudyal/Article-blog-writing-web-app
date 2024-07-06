from django.contrib.auth.forms import UserCreationForm  
from django import forms
from django.contrib.auth.models import User
from .models import Profiles

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    phone=forms.CharField(max_length=10)

    class Meta:
        model=User
        fields=['username','email','phone','password1','password2']


class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    phone=forms.CharField(max_length=10)

    class Meta:
        model=User
        fields=['username','email','phone']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profiles
        fields=['img'] 
