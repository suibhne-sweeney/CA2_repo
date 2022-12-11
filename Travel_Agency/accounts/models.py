from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), null=True, on_delete=models.CASCADE)
    dob = models.DateField(blank=False, null=False)
    gold_customer = models.BooleanField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to="profiles", blank=True, null=True)

    def __str__(self):
        return str(self.user)