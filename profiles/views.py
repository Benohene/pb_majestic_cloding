from django.shortcuts import render, get_object_or_404, reverse
from .models import UserProfile	
from .forms import UserProfileForm
from django.contrib import messages

from checkout.models import Order

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
    orders = profile.orders.all()
    
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }
    
    return render(request, template, context)


def order_history(request, order_number):
    """ A view to return the order history page """
    order = get_object_or_404(Order, order_number=order_number)
    
    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))
    
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True
    }
    
    return render(request, template, context)


def order_list(request):
    """ A view to return the profile page """
    # Get the user profile
    profile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        # If the request is a POST request, get the form data
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
    
    # If the request is a POST request, get the form data
    form = UserProfileForm(request.POST or None, instance=profile)
    orders = profile.orders.all()
    
    template = 'profiles/order_list.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }
    
    return render(request, template, context)