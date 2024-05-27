from django import forms
from django.forms import inlineformset_factory as inLineFormSetFactory
from .models import *

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['title']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']

QuestionFormSet = inLineFormSetFactory(Poll, Question, form=QuestionForm, extra=2, can_delete=True)