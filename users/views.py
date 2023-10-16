"""Views for Products App."""

from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from users.forms import LoginForm


class Login(FormView):
    template_name = 'users/login_form.html'
    form_class = LoginForm
    success_url = reverse_lazy('featured_product')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)
