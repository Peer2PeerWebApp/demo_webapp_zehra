from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    #full_name = models.CharField(max_length=100, blank=False)
    #age = models.PositiveIntegerField(null=True, blank=True)
    is_tutee = models.BooleanField(default=False)
    is_tutor = models.BooleanField(default=False)