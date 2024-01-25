"""Views for Payment App."""

import uuid
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm
from products.models import Product


@login_required
def check_out(request, product_id):
    """View for the integration with PayPal."""
    product = Product.objects.get(id=product_id)
    host = request.get_host()

    # Use sale_price if defined, otherwise use normal_price
    current_price = product.sale_price if product.sale_price is not None else product.normal_price

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': current_price,
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


@login_required
def payment_success(request, product_id):
    """View sends the product as context if the payment was successful."""
    product = Product.objects.get(id=product_id)
    return render(request, 'payment/payment_success.html', {'product': product})


@login_required
def payment_failed(request, product_id):
    """View sends the product as context if the payment failed."""
    product = Product.objects.get(id=product_id)
    return render(request, 'payment/payment_failed.html', {'product': product})
