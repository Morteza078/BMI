from django.urls import path

from .views import IndexView, BMIView

app_name = 'health'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('bmi/', BMIView.as_view(), name='BMI'),
]