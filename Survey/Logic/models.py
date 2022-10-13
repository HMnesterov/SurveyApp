from django.db import models

class Answer(models.Model):
    answer_text = models.CharField(
        '30'
    )
    is_true = models.BooleanField()




class Question(models.Model):
    text = models.TextField(max_length=1000)
    answers = models.ForeignKey(Answer, on_delete=models.CASCADE)


class Survey(models.Model):
    title = models.CharField(max_length=145)
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
