from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    users_voted = models.ManyToManyField(User, related_name='polls_voted', blank=True, null=True)

    def __str__(self):
        return self.question

class Choice(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=50)
    poll = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE, blank=True)
    votes = models.IntegerField(default=0)

    def __str__ (self):
        return self.text