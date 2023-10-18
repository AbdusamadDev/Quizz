from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from api.models import Questions, Answers
from api.serializers import QuestionSerializer, AnswerSerializer


class QuestionModelViewSet(ModelViewSet):
    model = Questions
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]
    queryset = Questions.objects.all()


class AnswerModelViewSet(ModelViewSet):
    model = Answers
    serializer_class = AnswerSerializer
    permission_classes = [AllowAny]
    queryset = Answers.objects.all()
