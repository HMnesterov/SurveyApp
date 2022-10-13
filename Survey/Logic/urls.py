from django.contrib import admin
from django.urls import path, re_path, include

from Logic.views import show_survey
from Survey import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('survey/<int:id>/', show_survey, name="show_survey"),
]

if settings.DEBUG:
    urlpatterns = [
        re_path(r'^admin/shell/', include('django_admin_shell.urls')),
    ] + urlpatterns

