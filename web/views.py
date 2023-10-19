from django.shortcuts import render
from api.models import Questions, Answers



def my_view(request):
    questions = Questions.objects.all()
    answers = Answers.objects.all()
    context = {"questions": questions, "answers": answers}
    return render(request, "home.html", context)
