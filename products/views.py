"""Views for Products App."""
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import View
from products.models import Product


class StaffRequiredMixin(object):
    """
    Mixin requirirá que el usuario sea staff o si no redirecciona a login de admin.
    """
    def dispatch(self, request, *args, **kwargs):
        """Función principal del mixin"""
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


class ProductListView(View):
    template_name = 'products/product_list.html'

    def get(self, request):
        # Recupera la lista de productos desde la base de datos
        products = Product.objects.all()

        # Add logic

        context = {
            'products': products,
        }

        return render(request, self.template_name, context)
