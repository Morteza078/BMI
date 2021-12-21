from django.urls import path

from health.api.views import BMIApiView

urlpatterns = [
    path('bmi/', BMIApiView.as_view(), name='BmiApi'),
]