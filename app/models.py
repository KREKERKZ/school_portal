# app/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    USER_TYPES = (
        ('parent', 'Parent'),
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Administrator'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    is_approved = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        verbose_name='user permissions',
    )


class Schedule(models.Model):
    course = models.CharField(max_length=100)
    day_of_week = models.CharField(max_length=50, default='Monday')
    start_time = models.TimeField(default=timezone.now)
    end_time = models.TimeField()
    teacher = models.ForeignKey('CustomUser', on_delete=models.CASCADE,
                                related_name='taught_classes')
    students = models.ManyToManyField('CustomUser',
                                      related_name='enrolled_classes')


class Grade(models.Model):
    student = models.ForeignKey('CustomUser', on_delete=models.CASCADE,
                                related_name='grades')
    course = models.ForeignKey('Schedule', on_delete=models.CASCADE,
                               related_name='grades', default=1)
    grade = models.FloatField()


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
