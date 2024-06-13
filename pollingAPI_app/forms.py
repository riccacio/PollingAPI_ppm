from django import forms
from django.forms import inlineformset_factory as inLineFormSetFactory
from .models import *

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question']

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text']

ChoiceFormSet = inLineFormSetFactory(Poll, Choice, form=ChoiceForm, extra=2, can_delete=True)