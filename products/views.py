"""Views for Products App."""
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect


class StaffRequiredMixin(object):
    """
    Mixin requirirá que el usuario sea staff o si no redirecciona a login de admin.
    """
    def dispatch(self, request, *args, **kwargs):
        """Función principal del mixin"""
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


def products_main(request):
    """
    Simple view to test functionality.
    """
    return render(request, 'pages/products.html', {})
