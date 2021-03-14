from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views
# from django.contrib.auth import views

urlpatterns = [
    path('', views.generate_key, name='generate-key-page'),
]