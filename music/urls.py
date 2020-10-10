from django.contrib import admin
from django.urls import path, include

from music import views

urlpatterns = [
    path('', views.ping),
]


