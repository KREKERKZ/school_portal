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
]
