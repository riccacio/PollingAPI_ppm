from rest_framework import serializers
from pollingAPI_app.models import Poll, Choice

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'

class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Poll
        fields = '__all__'