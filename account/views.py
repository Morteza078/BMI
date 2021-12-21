from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .forms import UserLoginForm, RegisterForm


# Create your views here.


class UserLoginView(LoginView):
    authentication_form = UserLoginForm
    template_name = "account/login.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if 'next' in request.GET:
                return HttpResponseRedirect(request.GET['next'])
            return redirect('health:index')
        return super().get(request, *args, **kwargs)


class RegisterView(View):
    form_class = RegisterForm
    template_name = 'account/register.html'
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
