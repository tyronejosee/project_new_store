"""Views for Payment App."""

import uuid
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm
from products.models import Product


def check_out(request, product_id):
    """Base view for the integration with PayPal."""
    product = Product.objects.get(id=product_id)
    host = request.get_host()
    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': product.normal_price,
        'item_name': product.title,
        'invoice': uuid.uuid4(),
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('payment:payment_success', kwargs = {'product_id': product.id})}",
        'cancel_url': f"http://{host}{reverse('payment:payment_failed', kwargs = {'product_id': product.id})}",
    }
    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)
    context = {
        'product': product,
        'paypal': paypal_payment
    }
    return render(request, 'payment/checkout.html', context)


def payment_success(request, product_id):
    """View sends the product as context if the payment was successful."""
    product = Product.objects.get(id=product_id)
    return render(request, 'payment/payment_success.html', {'product': product})


def payment_failed(request, product_id):
    """View sends the product as context if the payment failed."""
    product = Product.objects.get(id=product_id)
    return render(request, 'payment/payment_failed.html', {'product': product})
