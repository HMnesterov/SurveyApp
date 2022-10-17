from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from django.shortcuts import get_object_or_404


from .models import Survey, Submission
from .forms import SurveyForm, SurveyCreateForm


def main_page(request):
    Surveys = Survey.objects.all().order_by('title')
    contact_list = Surveys
    paginator = Paginator(contact_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "main_page.html", {'page_obj': page_obj, 'surveys': Surveys})


def show_survey(request, id=None):
    survey = get_object_or_404(Survey, pk=id)
    form = SurveyForm(survey)

    if request.method == "POST":
        form = SurveyForm(survey, request.POST)
        if form.is_valid():
            form.save()
            questions = survey.question_set.all()
            vichit_digit = 0
            count = 0
            user_right_vary = 0
            for question in questions:
                count += 1
                all_answ = question.choice_set.all()
                res = int(form.cleaned_data[f'question_{count}'])
                right_vary = [answer for answer in all_answ if answer.is_true]
                user_vary = all_answ[res - 1 - vichit_digit]

                if right_vary[0] == user_vary:
                    user_right_vary += 1
                vichit_digit += len(all_answ)


            return redirect('results', user_right_vary=user_right_vary, count=count)

    context = {
        "survey": survey,
        "form": form,
    }
    return render(request, "survey.html", context)



def show_test_results(request, user_right_vary, count):
    return render(request, 'results.html', {'right': user_right_vary, 'all': count})



def test(request):
    form = SurveyCreateForm()
    if request.method == "POST":
        form = SurveyCreateForm(request.POST)
        if form.is_valid():
            form.save()


    return render(request, 'test.html', {'form': form})