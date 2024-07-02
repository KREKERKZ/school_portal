# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Маршрут для домашней страницы
    path('grades/', views.view_grades, name='view_grades'),
    path('schedule/', views.view_schedule, name='view_schedule'),
    path('news/', views.view_news, name='view_news'),
    path('profile/', views.view_profile, name='view_profile'),
]
