

from django.contrib import admin
from django.urls import path
from resume.views import cv_index

urlpatterns = [
    path('', cv_index, name="index"),
]
