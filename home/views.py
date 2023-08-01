from django.shortcuts import render

# Create your views here.

def home(request):
    '''This is the home page view'''
    
    return render(request, 'home.html')
