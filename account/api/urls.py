from django.urls import path

from account.api.views import RegisterAPIView

urlpatterns = [
path('register/', RegisterAPIView.as_view(), name='register'),
]

