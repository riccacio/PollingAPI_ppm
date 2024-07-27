'''

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

'''

from django.urls import path
from .views import login_view, register, delete_account, dashboard, create_poll, delete_poll, submit_response, logout, RegisterView, LoginView, DeleteAccountView, PollListCreateView, PollDetailView, SubmitResponseView

urlpatterns = [
    # HTML views
    path('', login_view, name='login'),
    path('login/', login_view, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('delete_account/', delete_account, name='delete_account'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create_poll/', create_poll, name='create_poll'),
    path('delete_poll/<int:poll_id>/', delete_poll, name='delete_poll'),
    path('submit_response/<int:poll_id>/', submit_response, name='submit_response'),

    # API views
    path('api/register/', RegisterView.as_view(), name='api-register'),
    path('api/login/', LoginView.as_view(), name='api-login'),
    path('api/delete_account/', DeleteAccountView.as_view(), name='api-delete_account'),
    path('api/polls/', PollListCreateView.as_view(), name='api-polls-list_create'),
    path('api/polls/<int:pk>/', PollDetailView.as_view(), name='api-poll_detail'),
    path('api/polls/<int:poll_id>/responses/', SubmitResponseView.as_view(), name='api-submit_response'),
]
