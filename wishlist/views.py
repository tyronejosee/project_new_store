"""Views for Wishlist App."""

from django.shortcuts import render, redirect
from products.models import Product
from wishlist.models import Wishlist


def wishlist(request):
    """Render the wishlist view."""
    user = request.user
    wishlist, created = Wishlist.objects.get_or_create(user=user)
    products = wishlist.products.all()
    return render(request, "users/profile.html", {'wishlist': wishlist, 'products': products})


def add_product(request, product_id):
    """Add a product to the wishlist."""
    user = request.user
    product = Product.objects.get(id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=user)
    wishlist.add_product(product)
    return redirect("wishlist:wishlist")


def remove_product(request, product_id):
    """Remove a product from the wishlist."""
    user = request.user
    product = Product.objects.get(id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=user)
    wishlist.remove_product(product)
    return redirect("wishlist:wishlist")


def subtract_product(request, product_id):
    """Subtract a product from the wishlist."""
    user = request.user
    product = Product.objects.get(id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=user)
    wishlist.subtract_product(product)
    return redirect("wishlist:wishlist")
