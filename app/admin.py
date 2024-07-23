from django.contrib import admin
from .models import CustomUser, Grade, Schedule, News


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type', 'is_approved')
    list_filter = ('user_type', 'is_approved')
    search_fields = ('username', 'email')
    actions = ['approve_users']

    def approve_users(self, request, queryset):
        queryset.update(is_approved=True)
    approve_users.short_description = "Approve selected users"


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Grade)
admin.site.register(Schedule)
admin.site.register(News)
