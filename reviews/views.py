""" Reviews views """
from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Review
from .forms import ReviewForm


@login_required
def add_review(request, product_id):
    """Add a review for product with prodict id"""
    user = request.user
    product = get_object_or_404(Product, pk=product_id)

    # check if user has already reviewed this product
    review_exists = Review.objects.filter(
        user=user, product=product
    ).exists()
    # if user has already reviewed this product,
    # redirect to product detail page
    if review_exists:
        messages.error(
            request, "You have already reviewed this product"
        )
        return redirect(reverse("product_detail", args=[product.id]))
    # if user has not already reviewed this product, add review
    else:
        if request.method == "POST":
            form = ReviewForm(request.POST, request.FILES)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = user
                review.product = product
                review = form.save()
                messages.success(request, "Review added successfully")
                return redirect(
                    reverse("product_detail", args=[product.id])
                )
            else:
                messages.error(
                    request,
                    "Failed to add review. Please ensure the form is valid.",
                )
        else:
            form = ReviewForm()

        template = "reviews/add_review.html"
        context = {
            "form": form,
            "product": product,
            "reviews": review_exists,
        }

        return render(request, template, context)


@login_required
def edit_review(request, product_id, review_id):
    """Edit a review for product with prodict id"""
    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    # get review
    review = get_object_or_404(Review, pk=review_id)

    # if user is not the review owner or
    # superuser, redirect to product detail page
    if not user == review.user and not user.is_superuser:
        messages.error(request, "You cannot edit this review")
        return redirect(reverse("product_detail", args=[product.id]))
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = user
            review.product = product
            review = form.save()
            messages.success(request, "Review updated successfully")
            return redirect(
                reverse("product_detail", args=[product.id])
            )
        else:
            messages.error(
                request,
                "Failed to update review. Please ensure the form is valid.",
            )
    else:
        form = ReviewForm(instance=review)
        messages.info(
            request, f"You are editing your review for {product.name}"
        )

        template = "reviews/edit_review.html"
        context = {
            "form": form,
            "product": product,
            "review": review,
        }

        return render(request, template, context)


@login_required
def delete_review(request, product_id, review_id):
    """Delete a review for product with prodict id"""
    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    review = get_object_or_404(Review, pk=review_id)

    if not user == review.user and not user.is_superuser:
        messages.error(request, "You cannot delete this review")
        return redirect(reverse("product_detail", args=[product.id]))
    # if user is the review owner or superuser, delete review
    else:
        review.delete()
        messages.success(request, "Review deleted successfully")
        return redirect(reverse("product_detail", args=[product.id]))
