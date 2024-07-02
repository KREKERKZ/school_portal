# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),  # Включаем URL-шаблоны
    path('parent/', include('app.parent_routes')),
    path('student/', include('app.student_routes')),
    path('teacher/', include('app.teacher_routes')),
    path('admin/', include('app.admin_routes')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view
         (next_page='/'), name='logout'),
]
