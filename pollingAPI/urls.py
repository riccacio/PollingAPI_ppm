"""
URL configuration for pollingAPI project.

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
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from pollingAPI_app.views import *

urlpatterns = [
    path('', LoginView.as_view(template_name ='login.html'), name='login'),

    path('pollingAPI/', PollCreateView.as_view(), name='create_poll'),
    path('pollingAPI/<int:poll_id>/responses/', ResponseCreateView.as_view(), name='submit_response'),
    path('pollingAPI/<int:poll_id>/results/', PollResultsView.as_view(), name='poll_results'),

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', LoginView.as_view(template_name ='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

