from django.urls import path
from .views import *

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
    path('api/createPoll/', CreatePoll.as_view(), name='create-poll'),
    path('api/polls/', PollList.as_view(), name='api-polls-list'),
    path('api/polls/<int:pk>/', PollDetailView.as_view(), name='api-poll_detail'),
    path('api/polls/<int:poll_id>/createChoice/', CreateChoice.as_view(), name='create-choice'),
    path('api/polls/<int:poll_id>/choices/', ChoiceList.as_view(), name='choice_list'),
    path('api/polls/<int:poll_id>/choices/<int:choice_id>/vote/', VoteView.as_view(), name='vote'),
]
