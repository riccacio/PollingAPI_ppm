from rest_framework import serializers
from pollingAPI_app.models import Poll, Choice, Response

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    responses = ResponseSerializer(many=True, read_only=True)

    class Meta:
        model = Choice
        fields = '__all__'

class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = '__all__'