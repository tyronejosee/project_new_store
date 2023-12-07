"""Views for Management App."""

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from home.models import Page
from users.models import CustomUser
from products.models import Product
from management.forms import PageForm, ProductForm


class ManagementView(LoginRequiredMixin, TemplateView):
    """View for the management dashboard."""
    template_name = 'management/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # TODO: Add logic here

        # Sends context with the total number of products
        total_products = Product.objects.count()
        context['total_products'] = total_products
        return context


class PageListView(LoginRequiredMixin, ListView):
    """View for displaying a list of pages."""
    model = Page
    template_name = 'management/page_list.html'
    context_object_name = 'pages'
    paginate_by = 8


class PageUpdateView(LoginRequiredMixin, UpdateView):
    """View for updating a Page."""
    model = Page
    form_class = PageForm
    template_name = 'management/page_form.html'
    success_url = reverse_lazy('management:page_list')


class UserListView(LoginRequiredMixin, ListView):
    """View to display a list of users."""
    model = CustomUser
    template_name = 'management/user_list.html'
    context_object_name = 'users'


class ProductListView(LoginRequiredMixin, ListView):
    """View to display a list of available products."""
    model = Product
    template_name = 'management/product_list.html'
    context_object_name = 'products'
    paginate_by = 8

    def get_queryset(self):
        # Select specific fields from the 'Product' model using the 'only' method
        return Product.objects.filter(show_hide=True).only(
            'title', 'normal_price', 'image', 'stock',
            'featured', 'show_hide'
        )


class DeactivatedProductListView(LoginRequiredMixin, ListView):
    """View to display a list of deactivated products."""
    model = Product
    template_name = 'management/product_list.html'
    context_object_name = 'products'
    paginate_by = 8

    def get_queryset(self):
        # Select specific fields from the 'Product' model using the 'only' method
        return Product.objects.filter(show_hide=False).only(
            'title', 'normal_price', 'image', 'stock',
            'featured', 'show_hide'
        )


class ProductCreateView(LoginRequiredMixin, CreateView):
    """View to create a new product."""
    model = Product
    form_class = ProductForm
    template_name = 'management/product_form.html'
    success_url = reverse_lazy('management:product_list')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """"View to update a product's information."""
    model = Product
    form_class = ProductForm
    template_name = 'management/product_form.html'
    success_url = reverse_lazy('management:product_list')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """View to update a product's information."""
    model = Product
    success_url = None

    def post(self, request, pk, *args, **kwargs):
        # Retrieve the product by primary key (pk) and delete it logically
        object = Product.objects.get(id=pk)
        object.show_hide = False
        object.save()
        return redirect('management:product_list')


class ProductStatusToggleView(LoginRequiredMixin, DeleteView):
    """View to change a product's status (activate/deactivate)."""
    model = Product
    success_url = None

    def post(self, request, pk, action, *args, **kwargs):
        # Toggle the status of the product (deactivate or activate).
        product = Product.objects.get(id=pk)

        if action == "deactivate":
            product.show_hide = False
            product.save()
            return redirect('management:product_list')
        elif action == "activate":
            product.show_hide = True
            product.save()
            return redirect('management:product_deactivated_list')
