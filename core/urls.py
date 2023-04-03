from django.contrib import admin
from django.urls import path
from .views import HomeTemplateView
from core import views

urlpatterns = [
    path('', HomeTemplateView.as_view()),
    path('contact', views.contact, name='contact'),
]