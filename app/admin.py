from django.contrib import admin
from .models import CustomUser, Grade, Schedule, News

admin.site.register(CustomUser)
admin.site.register(Grade)
admin.site.register(Schedule)
admin.site.register(News)
