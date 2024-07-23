from django.urls import path
from . import views

urlpatterns = [
    path('grades/', views.view_grades, name='view_grades_student'),
    path('schedule/', views.view_schedule, name='view_schedule_student'),
    path('news/', views.view_news, name='view_news_student'),
    path('profile/', views.view_profile, name='view_profile_student'),
]
