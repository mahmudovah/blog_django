from django.contrib import admin

# Register your models here.
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'body', 'duration', 'duration_type', 'status', 'created_at', 'duration_range']

admin.site.register(Todo)