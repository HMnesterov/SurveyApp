from django import forms
from django.dispatch import receiver

from .models import Answer, Question, Survey, Submission


class SurveyForm(forms.Form):
    email = forms.EmailField()
    question_1 = forms.ChoiceField(widget=forms.RadioSelect, choices=())

    def __init__(self, survey, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.survey = survey
        del self.fields["question_1"]
        for question in survey.question_set.all():
            choices = [(choice.id, choice.text) for choice in question.choice_set.all()]
            self.fields[f"question_{question.id}"] = forms.ChoiceField(widget=forms.RadioSelect, choices=choices)
            self.fields[f"question_{question.id}"].label = question.text

