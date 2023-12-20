"""Views for Management App."""

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect

from home.models import Page
from users.models import CustomUser
from products.models import Product, Category, Brand, Deal
from management.forms import PageForm, ProductForm, CategoryForm, BrandForm, DealForm


# Main Views

class ManagementView(LoginRequiredMixin, TemplateView):
    """View for the management dashboard."""
    template_name = 'management/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Sends context with the total number of products
        total_products = Product.objects.count()
        context['total_products'] = total_products
        return context


# Page CRUD

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


# Product CRUD

class ProductListView(LoginRequiredMixin, ListView):
    """View to display a list of available products."""
    model = Product
    template_name = 'management/product_list.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        # Select specific fields from the 'Product' model using the 'only' method
        return Product.objects.filter(show_hide=True).only(
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


# Category CRUD

class CategoryListView(LoginRequiredMixin, ListView):
    """View to display a list of categories."""
    model = Category
    template_name = 'management/category_list.html'
    context_object_name = 'categories'
    paginate_by = 12


class CategoryCreateView(LoginRequiredMixin, CreateView):
    """View to create a new deal."""
    model = Category
    form_class = CategoryForm
    template_name = 'management/category_form.html'
    success_url = reverse_lazy('management:category_list')


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    """View for update a category."""
    model = Category
    form_class = CategoryForm
    template_name = 'management/category_form.html'
    success_url = reverse_lazy('management:category_list')


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    """View to delete a category."""
    model = Category
    template_name = 'management/category_confirm_delete.html'
    success_url = reverse_lazy('management:category_list')


# Brand CRUD

class BrandListView(LoginRequiredMixin, ListView):
    """View to display a list of brands."""
    model = Brand
    template_name = 'management/brand_list.html'
    context_object_name = 'brands'
    paginate_by = 12


class BrandCreateView(LoginRequiredMixin, CreateView):
    """View to create a new brand."""
    model = Brand
    form_class = BrandForm
    template_name = 'management/brand_form.html'
    success_url = reverse_lazy('management:brand_list')


class BrandUpdateView(LoginRequiredMixin, UpdateView):
    """View for update a brand."""
    model = Brand
    form_class = BrandForm
    template_name = 'management/brand_form.html'
    success_url = reverse_lazy('management:brand_list')


class BrandDeleteView(LoginRequiredMixin, DeleteView):
    """View to delete a brand."""
    model = Brand
    template_name = 'management/brand_confirm_delete.html'
    success_url = reverse_lazy('management:brand_list')


# Deal CRUD

class DealCreateView(LoginRequiredMixin, CreateView):
    """View to create a new deal."""
    model = Deal
    form_class = DealForm
    template_name = 'management/deal_form.html'
    success_url = reverse_lazy('management:deal_list')


class DealListView(LoginRequiredMixin, ListView):
    """View to display a list of deals."""
    model = Deal
    template_name = 'management/deal_list.html'
    context_object_name = 'deals'
    paginate_by = 12


class DealUpdateView(LoginRequiredMixin, UpdateView):
    """View for update a deal."""
    model = Deal
    form_class = DealForm
    template_name = 'management/deal_form.html'
    success_url = reverse_lazy('management:deal_list')


class DealDeleteView(LoginRequiredMixin, DeleteView):
    """View to delete a deal."""
    model = Deal
    template_name = 'management/deal_confirm_delete.html'
    success_url = reverse_lazy('management:deal_list')


# User CRUD

class UserListView(LoginRequiredMixin, ListView):
    """View to display a list of users."""
    model = CustomUser
    template_name = 'management/user_list.html'
    context_object_name = 'users'
