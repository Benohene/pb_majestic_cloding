'''A view to return the contact page'''
from django.shortcuts import render, redirect, reverse
from .forms import ContactMailForm


def contact(request):
    """A view to return the contact page"""

    if request.method == "POST":
        form = ContactMailForm(request.POST)

        if form.is_valid():
            print('form is valid')
            
            return redirect(reverse('home'))

    else:
        form = ContactMailForm()

    tewmplate = "contact/contact.html"    
    context = {
        "form": form,
    }
    return render(request, tewmplate, context)
