# app/urls.py

from django.urls import path
from . import views
from .auth import login_view, logout_view, register_view

urlpatterns = [
    path('', views.home_view, name='index'),
    path('grades/', views.view_grades, name='view_grades'),
    path('schedule/', views.view_schedule, name='view_schedule'),
    path('news/', views.view_news, name='view_news'),
    path('profile/', views.view_profile, name='view_profile'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('edit_schedule/', views.edit_schedule, name='edit_schedule'),
    path('edit_schedule/<int:schedule_id>/', views.edit_schedule,
         name='edit_schedule'),
    path('edit_grades/', views.edit_grades, name='edit_grades'),
    path('edit_grades/<int:grade_id>/', views.edit_grades, name='edit_grades'),
]
