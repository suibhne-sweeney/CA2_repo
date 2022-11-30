from django.db import models
from django.urls import reverse
import uuid
# Create your models here.

class Package(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    hotel = models.CharField(max_length=100, blank=True, null=True)
    tour = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to="locations")
    
    def __str__(self):
        return self.country







    

