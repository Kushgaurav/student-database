from django.contrib import admin

# Register your models here.

from .models import studentDetail

admin.site.register(studentDetail)


class studentAdmin(admin.ModelAdmin):
    list_display = ('fullName', 'collageId', 'subject', 'mobileNumber',
                    'email', 'date', 'file', 'course', 'created_at')
    list_filter = ('fullName', 'collageId', 'subject', 'mobileNumber',
                   'email', 'date', 'file', 'course', 'created_at')
    search_fields = ('fullName', 'collageId', 'subject', 'mobileNumber',
                     'email', 'date', 'file', 'course', 'created_at')
    ordering = ['created_at']
