from rest_framework.viewsets import ModelViewSet

from api.models import Questions, Answers


class QuestionModelViewSet(ModelViewSet):
    model = Questions
    