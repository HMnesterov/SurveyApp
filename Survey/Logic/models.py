from django.db import models




class Survey(models.Model):
    title = models.CharField(max_length=145)


class Question(models.Model):
    text = models.TextField(max_length=1000)

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)



class Answer(models.Model):
    answer_text = models.CharField(
        max_length=30
    )
    is_true = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class Submission(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    participant_email = models.EmailField(max_length=255)
    answer = models.ManyToManyField(Answer)
    status = models.CharField(max_length=255)

