from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import PollForm, ChoiceForm
from .models import Poll, Choice
from pollingAPI_app.serializers import *

def delete_account(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, 'Your account has been deleted.')
        return redirect('login')

class PollCreateView (generics.CreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAuthenticated]

class ResponseCreateView (generics.CreateAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
    permission_classes = [IsAuthenticated]

class PollResultsView (generics.RetrieveAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAuthenticated]

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')
        else:
            messages.error(request, 'There was an error creating your account.')
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def dashboard(request):
    polls = Poll.objects.all()
    choices = Choice.objects.all()
    return render(request, 'dashboard.html', {'polls': polls, 'choices': choices})


def polls_list(request):
    polls = Poll.objects.all()
    return render(request, 'polls_list.html', {'polls': polls})


def create_poll(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        options = request.POST.getlist('options')

        poll = Poll(question=question, user=request.user)
        poll.save()

        for option in options:
            choice = Choice(text=option, poll=poll)
            
            choice.save()

        return redirect('dashboard')

    return render(request, 'create_poll.html')


def delete_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    if request.user == poll.user:
        poll.delete()
    return redirect('dashboard')
