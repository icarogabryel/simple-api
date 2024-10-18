from django.contrib import admin
from .models import Task

# Register your models here.
class Tasks(admin.ModelAdmin):
    list_display = ['title', 'status', 'creation_date']
    search_fields = ['title', 'status']
    list_filter = ['status']

admin.site.register(Task, Tasks)
