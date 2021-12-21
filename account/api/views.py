from rest_framework import generics
from rest_framework.permissions import AllowAny

from account.api.serializers import RegisterSerializer
from account.models import CustomUser


class RegisterAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)