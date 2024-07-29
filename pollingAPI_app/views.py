from django.contrib.auth import login, authenticate, logout as auth_logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from pollingAPI_app.models import Poll, Choice
from pollingAPI_app.serializers import PollSerializer, ChoiceSerializer
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required


# HTML Views
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('dashboard')
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

@login_required
def dashboard(request):
    polls = Poll.objects.all().order_by('-created_at')
    choices = Choice.objects.all()
    return render(request, 'dashboard.html', {'polls': polls, 'choices': choices})

@login_required
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

@login_required
def delete_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    if request.user == poll.user:
        poll.delete()
    return redirect('dashboard')

@login_required
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

@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')


# API Views
class CreatePoll(generics.CreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PollList(generics.ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PollDetailView(generics.RetrieveAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CreateChoice(generics.CreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

    def perform_create(self, serializer):
        poll = get_object_or_404(Poll, id=self.kwargs.get('poll_id'))
        serializer.save(poll=poll)


class ChoiceList(generics.ListAPIView):
    serializer_class = ChoiceSerializer

    def get_queryset(self):
        poll_id = self.kwargs['poll_id']
        get_object_or_404(Poll, id=poll_id)
        return Choice.objects.filter(poll__id=poll_id)


class VoteView(APIView):
    def post(self, request, poll_id, choice_id):
        poll = get_object_or_404(Poll, id=poll_id)
        choice = get_object_or_404(Choice, id=choice_id, poll=poll)  # pass poll object instead of poll_id
        choice.votes += 1
        choice.save()
        poll.users_voted.add(request.user);
        poll.save()
        return Response({'message': 'Vote submitted successfully'}, status=status.HTTP_200_OK)
