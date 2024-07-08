# app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from .models import CustomUser, Grade, Schedule, News
from .forms import CustomUserCreationForm


def home_view(request):
    return render(request, 'index.html')


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if user.user_type == 'admin':
                user.is_approved = False
                messages.success(
                    request,
                    'Registration successful. Waiting for admin approval.')
            else:
                user.is_approved = True
                messages.success(request,
                                 'Registration successful. Please log in.')
            user.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def view_grades(request):
    if hasattr(request.user, 'user_type'):
        if request.user.user_type in ['parent', 'student']:
            grades = request.user.grades.all()
        elif request.user.user_type == 'teacher':
            grades = Grade.objects.filter(teacher=request.user)
        elif request.user.user_type == 'admin':
            grades = Grade.objects.all()
        else:
            grades = None
        return render(request, 'grades.html', {'grades': grades})
    else:
        return HttpResponse("User has no user_type attribute.")


@login_required
def view_schedule(request):
    if hasattr(request.user, 'user_type'):
        if request.user.user_type == 'teacher':
            schedules = request.user.schedules.all()
        elif request.user.user_type == 'admin':
            schedules = Schedule.objects.all()
        else:
            schedules = None
        return render(request, 'schedule.html', {'schedules': schedules})
    else:
        return HttpResponse("User has no user_type attribute.")


@login_required
def view_news(request):
    news = News.objects.all()
    return render(request, 'news.html', {'news': news})


@login_required
def view_profile(request):
    try:
        custom_user = CustomUser.objects.get(username=request.user.username)
        return render(request, 'profile.html', {'custom_user': custom_user})
    except CustomUser.DoesNotExist:
        return HttpResponse("User does not exist.")
