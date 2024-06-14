from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from pollingAPI_app.serializers import *


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


def delete_account(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, 'Your account has been deleted.')
        return redirect('login')


def dashboard(request):
    polls = Poll.objects.all().order_by('-created_at')
    choices = Choice.objects.all()
    return render(request, 'dashboard.html', {'polls': polls, 'choices': choices})

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

def submit_response(request, poll_id):
    if request.method == 'POST':
        choice_id = request.POST.get('choice')

        poll = get_object_or_404(Poll, id=poll_id)
        choice = get_object_or_404(Choice, id=choice_id, poll=poll)

        choice.votes += 1
        choice.save()

        poll.users_voted.add(request.user)
        poll.save()

    return redirect('dashboard')