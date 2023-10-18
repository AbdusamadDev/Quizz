from rest_framework import serializers

from api.models import Questions, Answers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = "__all__"
