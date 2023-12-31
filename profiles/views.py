'''This file contains the views for the profiles app. The profile view is'''
from django.shortcuts import (
    render,
    get_object_or_404,
    reverse,
    redirect,
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm
from .models import Wishlist


@login_required
def profile(request):
    """A view to return the profile page"""
    # Get the user profile
    profile = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.get_or_create(user=request.user)

    if request.method == "POST":
        # If the request is a POST request, get the form data
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")

    # If the request is a POST request, get the form data
    form = UserProfileForm(request.POST or None, instance=profile)
    orders = profile.orders.all()

    template = "profiles/profile.html"
    context = {
        "form": form,
        "orders": orders,
        "profile": profile,
        "wishlist": wishlist,
        "on_profile_page": True,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """A view to return the order history page"""
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(
        request,
        (
            f"This is a past confirmation for order number {order_number}. "
            "A confirmation email was sent on the order date."
        ),
    )

    template = "checkout/checkout_success.html"
    context = {"order": order, "from_profile": True}

    return render(request, template, context)


@login_required
def order_list(request):
    """A view to return the profile page"""
    # Get the user profile
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        # If the request is a POST request, get the form data
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.success(
                request,
                "Update failed. Please ensure the form is valid.",
            )
    else:
        # If the request is a POST request, get the form data
        form = UserProfileForm(request.POST or None, instance=profile)
    orders = profile.orders.all()

    template = "profiles/order_list.html"
    context = {"form": form, "orders": orders, "on_profile_page": True}

    return render(request, template, context)


# view wishlist
@login_required
def view_wishlist(request):
    """A view to return the wishlist page"""
    wishlist = Wishlist.objects.get_or_create(user=request.user)
    wishlist = wishlist[0]
    template = "profiles/wishlist.html"
    context = {
        "wishlist": wishlist,
    }
    return render(request, template, context)


# add to wishlist
@login_required
def add_to_wishlist(request, product_id):
    """Add a product to the wishlist"""
    product = get_object_or_404(Product, pk=product_id)
    wishlist = Wishlist.objects.get_or_create(user=request.user)
    wishlist = wishlist[0]
    wishlist.products.add(product)
    messages.success(request, f"{product.name} added to your wishlist")
    return redirect(request.META["HTTP_REFERER"])


# remove from wishlist
@login_required
def remove_from_wishlist(request, product_id):
    """Remove a product from the wishlist"""
    product = get_object_or_404(Product, pk=product_id)
    wishlist = Wishlist.objects.get(user=request.user)
    wishlist.products.remove(product)
    messages.success(
        request, f"{product.name} removed from your wishlist"
    )
    # return with HTTP REFERRER
    return redirect(request.META["HTTP_REFERER"])


# clear wishlist
@login_required
def clear_wishlist(request):
    """Clear the wishlist"""
    wishlist = Wishlist.objects.get(user=request.user)
    wishlist.products.clear()
    messages.success(request, "Your wishlist has been cleared")
    return redirect(reverse("view_wishlist"))
