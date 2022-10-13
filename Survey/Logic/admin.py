from django.contrib import admin

from django.contrib import admin
from .models import Survey, Question, Answer, Submission


class QuestionInline(admin.TabularInline):
    model = Question
    show_change_link = True


class ChoiceInline(admin.TabularInline):
    model = Answer


class SurveyAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline
    ]


class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        ChoiceInline
    ]


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('participant_email', 'status')


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Submission, SubmissionAdmin)