from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    is_tutee = models.BooleanField(default=False)
    is_tutor = models.BooleanField(default=False)