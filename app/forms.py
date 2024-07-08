# app/forms.py

from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'user_type', 'is_approved')

    is_approved = forms.BooleanField(label='Is Approved', required=False)
