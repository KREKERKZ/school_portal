# app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.contrib import messages
from .models import CustomUser, Grade, Schedule, News
from .forms import CustomUserCreationForm, ScheduleForm, GradeForm


def home_view(request):
    return render(request, 'index.html')


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if user.user_type == 'admin':
                if request.user.is_superuser:
                    user.is_approved = False
                    messages.success(
                        request,
                        'Registration successful. Waiting for admin approval.')
                else:
                    messages.error(
                        request,
                        'Only superusers can approve admin registrations.')
                    return redirect('register')
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
        if request.user.user_type == 'parent':
            grades = Grade.objects.filter(student__parent=request.user)
        elif request.user.user_type == 'student':
            grades = Grade.objects.filter(student=request.user)
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
            schedules = Schedule.objects.filter(teacher=request.user)
        elif request.user.user_type == 'student':
            schedules = Schedule.objects.filter(student=request.user)
        elif request.user.user_type == 'admin':
            schedules = Schedule.objects.all()
        else:
            schedules = None
        return render(request, 'schedule.html', {'schedules': schedules})
    else:
        return HttpResponse("User has no user_type attribute.")


@user_passes_test(lambda u: u.is_staff or u.user_type == 'teacher')
@login_required
def edit_schedule(request, schedule_id=None):
    if schedule_id:
        schedule = get_object_or_404(Schedule, id=schedule_id)
    else:
        schedule = None

    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('view_schedule')
    else:
        form = ScheduleForm(instance=schedule)
        schedules = Schedule.objects.all()
        teachers = CustomUser.objects.filter(user_type='teacher')
        return render(request, 'edit_schedule.html', {'form': form,
                                                      'schedules': schedules,
                                                      'teachers': teachers})


@user_passes_test(lambda u: u.user_type == 'teacher')
@login_required
def edit_grades(request, grade_id=None):
    if grade_id:
        grade = get_object_or_404(Grade, id=grade_id)
    else:
        grade = None

    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('view_grades')
    else:
        form = GradeForm(instance=grade)
        grades = Grade.objects.all()
        students = CustomUser.objects.filter(user_type='student')
        courses = Schedule.objects.all()
        return render(request, 'edit_grades.html', {'form': form,
                                                    'grades': grades,
                                                    'students': students,
                                                    'courses': courses})


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
