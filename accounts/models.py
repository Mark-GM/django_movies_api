from django.db import models
from django.contrib.auth.models import AbstractUser


class ITIUser(AbstractUser):
    mobile_number = models.CharField(max_length=50, blank=True, null=True)
