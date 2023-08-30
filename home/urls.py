"""This file is used to map the urls to the views"""
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("faq/", views.faq, name="faq"),
]
