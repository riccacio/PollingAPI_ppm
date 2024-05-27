from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Question(models.Model):
    text = models.CharField(max_length=250)
    poll = models.ForeignKey(Poll, related_name='question', on_delete=models.CASCADE)

    def __str__ (self):
        return self.text

class Response(models.Model):
    answer = models.CharField(max_length=250)
    poll = models.ForeignKey(Poll, related_name='response', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='responses', on_delete=models.CASCADE)

    def __str__ (self):
        return self.answer