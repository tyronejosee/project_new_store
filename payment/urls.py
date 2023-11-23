"""URLs for Payment App."""

from django.urls import path
from payment.views import check_out, payment_success, payment_failed

app_name = 'payment'

urlpatterns = [
    path('checkout/<int:product_id>/', check_out, name='checkout'),
    path('payment-success/<int:product_id>/', payment_success, name='payment_success'),
    path('payment-failed/<int:product_id>/', payment_failed, name='payment_failed'),
]
