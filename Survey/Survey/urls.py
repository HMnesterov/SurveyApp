from django.urls import path, include
from Logic import urls

urlpatterns = [
    path('', include(urls)),
]
