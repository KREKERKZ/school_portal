from django.urls import path
from . import views

urlpatterns = [
    path('grades/', views.view_grades, name='view_grades_admin'),
    path('schedule/', views.view_schedule, name='view_schedule_admin'),
    path('news/', views.view_news, name='view_news_admin'),
    path('profile/', views.view_profile, name='view_profile_admin'),
]
