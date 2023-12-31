"""This file contains the views for the cart app. The cart app is used to add,
adjust and delete items from the cart."""
from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
)
from django.http import HttpResponse
from django.contrib import messages
from products.models import Product


# Create your views here.
def view_cart(request):
    """A view that renders the cart contents page"""
    return render(request, "cart/cart.html")


def add_to_cart(request, item_id):
    """Add a quantity of the specified product to the cart"""

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    size = None
    if "product_size" in request.POST:
        size = request.POST["product_size"]
    cart = request.session.get("cart", {})

    if size:
        if item_id in list(cart.keys()):
            # If the item is already in the cart
            if size in cart[item_id]["items_by_size"].keys():
                cart[item_id]["items_by_size"][size] += quantity
                messages.success(
                    request,
                    f'Updated size {size.upper()} {product.name} quantity to '
                    f'{cart[item_id]["items_by_size"][size]}',
                )
            else:
                cart[item_id]["items_by_size"][size] = quantity
                messages.success(
                    request,
                    f"Added size {size.upper()} {product.name} to your cart",
                )
        else:
            cart[item_id] = {"items_by_size": {size: quantity}}
            messages.success(
                request,
                f"Added size {size.upper()} {product.name} to your cart",
            )
        # stock control
        if cart[item_id]["items_by_size"][size] > product.stock:
            cart[item_id]["items_by_size"][size] = product.stock
            messages.error(
                request,
                f"You have exceeded the available stock of this item. "
                f"The maximum quantity available is {product.stock}.",
            )
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(
                request,
                f"Updated {product.name} quantity to {cart[item_id]}",
            )
        else:
            cart[item_id] = quantity
            messages.success(
                request, f"Added {product.name} to your cart"
            )
        # stock control
        if cart[item_id] > product.stock:
            cart[item_id] = product.stock
            messages.error(
                request,
                f"You have exceeded the available stock of this item. "
                f"The maximum quantity available is {product.stock}.",
            )

    request.session["cart"] = cart
    return redirect(redirect_url)


# Update the quantity of the specified product to the specified amount
def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    size = None
    if "product_size" in request.POST:
        size = request.POST["product_size"]
    cart = request.session.get("cart", {})

    if size:
        if quantity > 0:
            cart[item_id]["items_by_size"][size] = quantity
            messages.success(
                request,
                f'Updated size {size.upper()} {product.name} '
                f'quantity to {cart[item_id]["items_by_size"][size]}',
            )
        else:
            del cart[item_id]["items_by_size"][size]
            if not cart[item_id]["items_by_size"]:
                cart.pop(item_id)
                messages.success(
                    request,
                    f"Removed size {size.upper()} {product.name} "
                    f"from your cart",
                )
        # stock control
        if cart[item_id]["items_by_size"][size] > product.stock:
            cart[item_id]["items_by_size"][size] = product.stock
            messages.error(
                request,
                f"You have exceeded the available stock of this item. "
                f"The maximum quantity available is {product.stock}.",
            )
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(
                request,
                f"Updated {product.name} quantity to {cart[item_id]}",
            )
        else:
            cart.pop(item_id)
            messages.success(
                request, f"Removed {product.name} from your cart"
            )
        # stock control
        if cart[item_id] > product.stock:
            cart[item_id] = product.stock
            messages.error(
                request,
                f"You have exceeded the available stock of this item. "
                f"The maximum quantity available is {product.stock}.",
            )

    request.session["cart"] = cart
    return redirect(reverse("view_cart"))


# Remove the item from the cart
def delete_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if "product_size" in request.POST:
            size = request.POST["product_size"]
        cart = request.session.get("cart", {})

        if size:
            del cart[item_id]["items_by_size"][size]
            if not cart[item_id]["items_by_size"]:
                cart.pop(item_id)
                messages.success(
                    request,
                    f"Removed size {size.upper()} {product.name} "
                    f"from your cart",
                )
        else:
            cart.pop(item_id)
            messages.success(
                request, f"Removed {product.name} from your cart"
            )

        request.session["cart"] = cart
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)
