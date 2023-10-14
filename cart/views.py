"""Views for Cart App."""

from django.shortcuts import render, redirect
from products.models import Product
from cart.cart import Cart


def store(request):
    """Pending."""
    products = Product.objects.all()
    return render(request, "cart/cart_list.html", {'products': products})


def add_product(request, product_id):
    """Pending."""
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product)
    return redirect("cart:store")


def remove_product(request, product_id):
    """Pending."""
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.remove(product)
    return redirect("cart:store")


def subtract_product(request, product_id):
    """Pending."""
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.subtract(product)
    return redirect("cart:store")


def clear_cart(request):
    """Pending."""
    cart = Cart(request)
    cart.clear()
    return redirect("cart:store")
