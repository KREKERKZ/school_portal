# app/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    USER_TYPES = (
        ('parent', 'Parent'),
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Administrator'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES)


class Grade(models.Model):
    student = models.ForeignKey(CustomUser,
                                on_delete=models.CASCADE,
                                related_name='grades')
    subject = models.CharField(max_length=100)
    grade = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()


class Schedule(models.Model):
    teacher = models.ForeignKey(CustomUser,
                                on_delete=models.CASCADE,
                                related_name='schedules')
    day = models.CharField(max_length=20)
    time = models.TimeField()
    class_name = models.CharField(max_length=100)


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
