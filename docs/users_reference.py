from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserCreationForm

class RegisterView(View):
    template_name = 'registration/register.html'

    def get(self, request):
        data = {'form': CustomUserCreationForm()}
        return render(request, self.template_name, data)

    def post(self, request):
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
        else:
            data = {'form': user_creation_form}
            return render(request, self.template_name, data)