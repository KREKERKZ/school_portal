# app/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Grade, Schedule, News  # Импортируем CustomUser


@login_required
def view_grades(request):
    if request.user.user_type == 'parent':
        grades = request.user.grades.all()
    elif request.user.user_type == 'student':
        grades = request.user.grades.all()
    elif request.user.user_type == 'teacher':
        grades = Grade.objects.filter(teacher=request.user)
    elif request.user.user_type == 'admin':
        grades = Grade.objects.all()
    else:
        grades = None
    return render(request, 'grades.html', {'grades': grades})


@login_required
def view_schedule(request):
    if request.user.user_type == 'teacher':
        schedules = request.user.schedules.all()
    elif request.user.user_type == 'admin':
        schedules = Schedule.objects.all()
    else:
        schedules = None
    return render(request, 'schedule.html', {'schedules': schedules})


@login_required
def view_news(request):
    news = News.objects.all()
    return render(request, 'news.html', {'news': news})


@login_required
def view_profile(request):
    custom_user = CustomUser.objects.get(user=request.user)
    return render(request, 'profile.html', {'custom_user': custom_user})
