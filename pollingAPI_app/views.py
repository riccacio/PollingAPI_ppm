from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import PollForm, QuestionForm
from .models import Poll
from pollingAPI_app.serializers import *
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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request=request, username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')

    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form':form})

def dashboard(request):
    return render(request, 'dashboard.html')