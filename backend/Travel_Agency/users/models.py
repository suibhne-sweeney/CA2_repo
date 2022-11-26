from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    phone_num = models.PositiveIntegerField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)