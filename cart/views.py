"""Views for Cart App."""

from django.views.generic import TemplateView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.urls import reverse_lazy
from cart.models import Cart, CartItem
from cart.forms import AddToCartForm


class CartView(TemplateView):
    """Pending."""
    template_name = 'cart/cart_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        context['cart'] = cart
        return context


class AddToCartView(FormView):
    """Pending."""
    form_class = AddToCartForm
    template_name = 'cart/cart_add.html'
    success_url = reverse_lazy('cart')
    # success_url = '/cart/'

    def form_valid(self, form):
        """Pending."""
        product = form.cleaned_data['product']
        quantity = form.cleaned_data['quantity']
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        cart.products.add(product, through_defaults={'quantity': quantity})
        return super().form_valid(form)


class UpdateCartView(UpdateView):
    """Pending."""
    pass


class RemoveFromCartView(DeleteView):
    """Pending."""
    model = CartItem
    template_name = 'cart/cart_remove.html'
    success_url = reverse_lazy('cart')
