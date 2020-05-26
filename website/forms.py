from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    username=forms.EmailField(max_length=200)
    class Meta:
        model=User
        fields=('first_name','last_name','username','password1','password2')