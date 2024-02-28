"""
URL configuration for nimap2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from client import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', views.client_list, name='client-list'),
    path('clients/<int:pk>/', views.client_detail, name='client-detail'),
    path('clients/<int:pk>/projects/', views.client_projects, name='client-projects'),
    path('clients/<int:pk>/projects/create/', views.create_project, name='create-project'),
    path('projects/', views.user_projects, name='user-projects'),

]

