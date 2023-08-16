from django.shortcuts import render, get_object_or_404
from .models import UserProfile	
from .forms import UserProfileForm
from django.contrib import messages

# Create your views here.

def profile(request):
    """ A view to return the profile page """
    # Get the user profile
    profile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        # If the request is a POST request, get the form data
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
    
    # If the request is a POST request, get the form data
    form = UserProfileForm(request.POST or None, instance=profile)
    order_history = profile.orders.all()
    
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'order_history': order_history,
        'on_profile_page': True
    }
    
    return render(request, template, context)