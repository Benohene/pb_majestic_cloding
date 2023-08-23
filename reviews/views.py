from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Product
from .models import Review
from .forms import ReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

# Add a review for product with prodict id
# Code adapted from Code Institute Boutique Ado project
@login_required
def add_review(request, product_id):
    # get product
    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    
    # check if user has already reviewed this product
    review_exists = Review.objects.filter(user=user, product=product).exists()
    # if user has already reviewed this product, redirect to product detail page
    if review_exists:
        messages.error(request, 'You have already reviewed this product')
        return redirect(reverse('product_detail', args=[product.id]))
    # if user has not already reviewed this product, add review
    else:
        if request.method == 'POST':
            form = ReviewForm(request.POST, request.FILES)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = user
                review.product = product
                review = form.save()
                messages.success(request, 'Review added successfully')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, 'Failed to add review. Please ensure the form is valid.')
        else:
            form = ReviewForm()
            
        template = 'reviews/add_review.html'
        context = {
            'form': form,
            'product': product,
            'reviews': review_exists,
        }
        
        return render(request, template, context)
    
# Edit a review for product with prodict id

@login_required
def edit_review(request, review_id):
    # get product
    user = request.user
    review = get_object_or_404(Review, pk=review_id)
    product = get_object_or_404(Product, pk=review.product.id)
    
    # check if user has already reviewed this product
    review_exists = Review.objects.filter(user=user, product=product).exists()
    # if user has already reviewed this product, redirect to product detail page
    if review_exists:
        messages.error(request, 'You have already reviewed this product')
        return redirect(reverse('product_detail', args=[product.id]))
    # if user has not already reviewed this product, add review
    else:
        if user.is_superuser or user == review.user:
            if request.method == 'POST':
                form = ReviewForm(request.POST, request.FILES, instance=review)
                if form.is_valid():
                    review = form.save(commit=False)
                    review.user = user
                    review.product = product
                    review = form.save()
                    messages.success(request, 'Review updated successfully')
                    return redirect(reverse('product_detail', args=[product.id]))
                else:
                    messages.error(request, 'Failed to update review. Please ensure the form is valid.')
            else:
                form = ReviewForm(instance=review)
        else:
            messages.error(request, 'You do not have permission to edit this review')
            return redirect(reverse('product_detail', args=[product.id]))
            
        template = 'reviews/edit_review.html'
        context = {
            'form': form,
            'product': product,
            'review': review,
        }
        
        return render(request, template, context)