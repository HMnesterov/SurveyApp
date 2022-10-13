from django.shortcuts import render

from django.shortcuts import get_object_or_404
from .models import Survey
from .forms import SurveyForm


def index(request):
    return render(request, "base.html")


def show_survey(request, id=None):
    survey = get_object_or_404(Survey, pk=id)
    form = SurveyForm(survey)

    context = {
        "survey": survey,
        "form": form,
    }
    return render(request, "base.html", context)
