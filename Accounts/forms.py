from .models import Request
from django.forms import DateInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['request_type', 'start_date', 'end_date', 'reason']
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date': DateInput(attrs={'type': 'date'})
        }
