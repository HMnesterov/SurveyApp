from django.db import models
from django.urls import reverse


class Survey(models.Model):
    title = models.CharField(max_length=145)


    def return_link(self):
        return reverse('show_survey', args=[self.pk])


    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.TextField(max_length=1000)

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)



class Answer(models.Model):
    text = models.CharField(
        max_length=30
    )
    is_true = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choice_set')


class Submission(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    answer = models.ManyToManyField(Answer)
    status = models.CharField(max_length=255)

