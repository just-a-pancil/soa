from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
# from django.contrib.auth import views
from . import views

urlpatterns = [
    path('choose_class_please/', views.choose_class_please, name="choose_class_please"),]