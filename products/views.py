""" This file will contain all the views for the products app """
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    reverse,
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg
from django.db.models.functions import Lower
from profiles.models import Wishlist
from reviews.models import Review
from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """A view to show all products, including sorting and search queries"""
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    # wishlist
    if request.user.is_authenticated:
        wishlist = Wishlist.objects.get_or_create(user=request.user)
    else:
        wishlist = None

    if request.GET:
        # Sorting functionality
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(
                    lower_name=Lower("name")
                )  # This will sort the products by name in ascending order
            if sortkey == "category":
                sortkey = "category__name"
            if sortkey == "price":
                sortkey = "price"
            if sortkey == "rating":
                sortkey = "rating"
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Search functionality
        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "Your search cannot be found!")
                return redirect(reverse("products"))
            queries = Q(name__icontains=query) | Q(
                description__icontains=query
            )
            products = products.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
        "current_direction": direction,
        "wishlist": wishlist,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """A view to show individual product details"""
    product = get_object_or_404(Product, pk=product_id)
    user = request.user
    reviews = Review.objects.filter(product=product)
    rating_avg = reviews.aggregate(Avg("review_rating"))[
        "review_rating__avg"
    ]

    if user.is_authenticated:
        wishlist = Wishlist.objects.get_or_create(user=user)
        review_user = Review.objects.filter(
            user=user, product=product
        ).exists()
    else:
        wishlist = None
        review_user = None

    context = {
        "product": product,
        "reviews": reviews,
        "wishlist": wishlist,
        "rating_avg": rating_avg,
        "review_user": review_user,
    }

    return render(request, "products/product_detail.html", context)


@login_required
def add_product(request):
    """A view to add products to the store"""
    if not request.user.is_superuser:
        messages.error(
            request,
            "Sorry, only store owners can get access to this page.",
        )
        return redirect(reverse("home"))
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # This will save the form
            product = form.save()
            messages.success(request, "Successfully added product!")
            return redirect(
                reverse("product_detail", args=[product.id])
            )
        else:
            messages.error(
                request,
                "Failed to add product. Please ensure the form is valid.",
            )
    else:
        form = ProductForm()
    template = "products/add_product.html"
    context = {
        "form": form,
    }
    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """A view to edit products in the store"""
    if not request.user.is_superuser:
        messages.error(
            request,
            "Sorry, only store owners can get access to this page.",
        )
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        # This will save the form
        form = ProductForm(
            request.POST, request.FILES, instance=product
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated product!")
            return redirect(
                reverse("product_detail", args=[product.id])
            )
        else:
            messages.error(
                request,
                "Failed to update product. Please ensure the form is valid.",
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")
    template = "products/edit_product.html"
    context = {
        "form": form,
        "product": product,
    }
    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """A view to delete products from the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, "Product deleted!")
    return redirect(reverse("products"))
