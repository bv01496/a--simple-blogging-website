from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(max_length=20, required=False)
    last_name = forms.CharField(max_length=20, required=False)
    class Meta:
        model = User
        fields = ['username','email','password1','password2','first_name','last_name']
