from django.contrib import admin
from django.urls import path, include
from pollingAPI_app.views import *

urlpatterns = [
    path('', login_view, name='login'),

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create_poll/', create_poll, name='create_poll'),
    path('delete_account/', delete_account, name='delete_account'),
    path('delete_poll/<int:poll_id>/', delete_poll, name='delete_poll'),

    path('poll/<int:poll_id>/submit_response/', submit_response, name='submit_response'),
]