from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views import View

from health.forms import BMIForm


class IndexView(View):
    def get(self, request):
        return render(request, "health/index.html", )


class BMIView(LoginRequiredMixin,View):
    form_class = BMIForm
    template_name = 'health/bmi.html'
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
