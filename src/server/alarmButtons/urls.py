
from django.contrib import admin
from django.urls import path
from .views import Buttons

from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('', csrf_exempt(Buttons.as_view())),
]