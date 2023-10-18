from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from api.models import Questions, Answers, Results
from api.serializers import (
    QuestionSerializer,
    AnswerSerializer,
    ResultSerializer,
)


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


class SubmitAPIView(ListCreateAPIView):
    model = Results
    serializer_class = ResultSerializer
    queryset = Results.objects.all().order_by("-count")

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        count = 0
        for data in serializer.validated_data.get("answers"):
            question = Questions.objects.get(pk=data.get("pk"))
            if data.get("chosen") == question.correct_answer:
                count += 1
        return Response(data={"msg": str(count)})
