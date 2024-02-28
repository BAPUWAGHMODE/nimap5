# admin.py

from django.contrib import admin
from .models import Client, Project, UserProject

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'created_at', 'created_by')
    search_fields = ('client_name', 'created_by__username')
    list_filter = ('created_at', 'created_by')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'client', 'created_at', 'created_by')
    search_fields = ('project_name', 'client__client_name', 'created_by__username')
    list_filter = ('created_at', 'created_by')

@admin.register(UserProject)
class UserProjectAdmin(admin.ModelAdmin):
    list_display = ('user', 'project')
    search_fields = ('user__username', 'project__project_name')
