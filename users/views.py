"""Views for Users App."""

from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from users.models import CustomUser
from users.forms import UserLoginForm, UserRegistrationForm


class UserLoginView(FormView):
    """View for user login."""
    template_name = 'users/login_form.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('home:index')

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
    """View for user registration."""
    model = CustomUser
    form_class = UserRegistrationForm
    template_name = 'users/registration_form.html'
    success_url = reverse_lazy('cart:cart')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

    def get_success_url(self):
        return self.success_url


class UserPasswordChangeView(PasswordChangeView):
    """View for password change."""
    template_name = 'users/password_change_form.html'
    success_url = reverse_lazy('users:password_change-done')


@login_required
def user_logout(request):
    """Closes the current user's session and redirects them to the site's homepage."""
    logout(request)
    return HttpResponseRedirect('/')
