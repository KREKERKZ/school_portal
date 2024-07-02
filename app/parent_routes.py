from django.urls import path
from . import views

urlpatterns = [
    path('grades/', views.view_grades, name='view_grades_parent'),
    path('schedule/', views.view_schedule, name='view_schedule_parent'),
    path('news/', views.view_news, name='view_news_parent'),
    path('profile/', views.view_profile, name='view_profile_parent'),
    # Добавьте другие маршруты для родителей, если есть
]
