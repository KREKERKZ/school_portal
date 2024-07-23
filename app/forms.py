# app/forms.py

from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser, Schedule, Grade


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'user_type')


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['course', 'day_of_week', 'start_time', 'end_time',
                  'teacher', 'students']


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'course', 'grade']
