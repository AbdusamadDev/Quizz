from rest_framework import serializers

from api.models import Questions, Answers, Results


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer()

    class Meta:
        model = Questions
        fields = "__all__"

    def create(self, validated_data):
        answers_data = validated_data.pop("answers")
        answers_instance = Answers.objects.create(**answers_data)
        question = Questions.objects.create(answers=answers_instance, **validated_data)
        return question


class ResultSerializer(serializers.Serializer):
    fullname = serializers.CharField(required=True)
    answers = serializers.ListField(required=True)


class ResultGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = "__all__"
