from django.db import models


class Answers(models.Model):
    CHOICES = (
        ("a", "Answer A"),
        ("b", "Answer B"),
        ("c", "Answer C"),
    )

    a = models.CharField(max_length=200)
    b = models.CharField(max_length=200)
    c = models.CharField(max_length=200)
    correct_answer = models.CharField(choices=CHOICES, max_length=50)


class Questions(models.Model):
    text = models.CharField(max_length=500)
    answers = models.ForeignKey(to=Answers, on_delete=models.CASCADE)
