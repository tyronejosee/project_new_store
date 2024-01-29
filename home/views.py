"""Views for Home App."""

from django.views.generic import TemplateView, DetailView
from django.shortcuts import render
from home.models import Page
from products.models import Product
from users.forms import ThemePreferenceForm


class IndexTemplateView(TemplateView):
    """View for rendering the site index with multiple contexts."""
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        # Sends multiple contexts to the templates
        context = super().get_context_data(**kwargs)

        # All the products (12 prods.)
        context['all_products'] = Product.objects.filter(
            show_hide=True, stock__gte=1
        ).order_by('title')[:12]

        # Recent products (12 prods.)
        context['recent_products'] = Product.objects.filter(
            show_hide=True, stock__gte=1
        ).order_by('-updated_at')[:12]

        # Apple (brand) (6 prods.)
        context['apple'] = Product.objects.filter(
            show_hide=True, stock__gte=1, brand__name__iexact='apple'
        ).order_by('-updated_at')[:6]

        # Samsung (brand) (6 prods.)
        context['samsung'] = Product.objects.filter(
            show_hide=True, stock__gte=1, brand__name__iexact='samsung'
        ).order_by('-updated_at')[:6]

        # Computer monitors (category) (6 prods.)
        context['computer_monitors'] = Product.objects.filter(
            show_hide=True, stock__gte=1, category__title__iexact='computer monitors'
        ).order_by('-updated_at')[:6]

        return context

    def post(self, request, *args, **kwargs):
        """Overrides to handle POST requests."""
        # Handle ThemePreferenceForm submission
        theme_form = ThemePreferenceForm(request.POST)
        if theme_form.is_valid():
            theme_preference = theme_form.cleaned_data['theme_preference']
            request.session['theme_preference'] = theme_preference

        # Add theme_form to the context
        context = self.get_context_data(**kwargs)
        context["theme_form"] = theme_form

        return render(request, self.template_name, context)


class PageDetailView(DetailView):
    """View to display details of the static pages of the site."""
    model = Page
    template_name = 'home/page_detail.html'
    context_object_name = 'page'

    def get_object(self, queryset=None):
        # Gets a key from the HTML to be used as a filter in the query
        key = self.kwargs['key']
        return Page.objects.get(key=key)
