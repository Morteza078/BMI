from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    length = models.FloatField(default=0)
    weight = models.FloatField(default=0)

    class Meta:
        verbose_name = "Custom user"
        verbose_name_plural = "Custom users"
