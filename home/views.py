"""This is the home app views"""
from django.shortcuts import render


def home(request):
    """This is the home page view"""

    return render(request, "home.html")


def faq(request):
    """A view to return the faq page"""
    return render(request, "home/faq.html")
