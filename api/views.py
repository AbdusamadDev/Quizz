from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from api.models import Questions, Answers, Results
from api.serializers import (
    QuestionSerializer,
    AnswerSerializer,
    ResultSerializer,
    ResultGETSerializer,
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


class SubmitAPIView(CreateAPIView):
    model = Results
    serializer_class = ResultSerializer
    queryset = Results.objects.all().order_by("-count")

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        count = 0
        users = Results.objects.all().values_list("fullname")
        users = [user[0] for user in users]
        print(users)
        if serializer.validated_data.get("fullname") in users:
            return Response(
                data={"msg": "You have already taken the quizz"},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )
        for data in serializer.validated_data.get("answers"):
            question = Questions.objects.get(pk=data.get("question_id"))
            answer = Answers.objects.get(pk=question.answers.pk)
            if data.get("answer") == answer.correct_answer:
                count += 1
        total = Questions.objects.all().count()
        percentage = (count / total) * 100
        Results.objects.create(
            fullname=serializer.validated_data.get("fullname"),
            count=count,
            percentage=percentage,
        )
        rank = ResultGETSerializer(self.get_queryset(), many=True).data
        return Response(rank, status=status.HTTP_201_CREATED)


"""
{
    "fullname": "Abdusamad Abdullaxanov",
    "answers": [
        {
            "question_id": 1,
            "answer": "a"
        },
        {
            "question_id": 1,
            "answer": "c"
        }

    ]
}
"""
