from django.contrib import admin
from django.urls import path, re_path, include

from Logic.views import show_survey, main_page, show_test_results, test
from Survey import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('survey/<int:id>/', show_survey, name="show_survey"),
    path('', main_page, name='main_page'),
    path('survey/results/<int:user_right_vary>/<int:count>/', show_test_results, name='results'),
    path('test/', test, name='test')
]

if settings.DEBUG:
    urlpatterns = [
        re_path(r'^admin/shell/', include('django_admin_shell.urls')),
    ] + urlpatterns

