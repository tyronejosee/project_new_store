"""Views for Cart App."""

from django.shortcuts import render, redirect
from cart.cart import Cart
from products.models import Product


def store(request):
    products = Product.objects.all()
    return render(request, "cart/cart_list.html", {'products': products})


def add_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product)
    return redirect("cart:store")


def remove_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.remove(product)
    return redirect("cart:store")


def subtract_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.subtract(product)
    return redirect("cart:store")


def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart:store")
