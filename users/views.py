"""Views for Users App."""

from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from users.models import CustomUser
from users.forms import UserLoginForm, UserRegistrationForm


class UserLoginView(FormView):
    """Class-based view for user login."""
    template_name = 'users/login_form.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('featured_product')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(UserLoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(UserLoginView, self).form_valid(form)


class UserRegistrationView(CreateView):
    """Class-based view for user registration."""
    model = CustomUser
    form_class = UserRegistrationForm
    template_name = 'users/registration_form.html'
    success_url = 'featured_product'
