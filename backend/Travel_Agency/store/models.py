from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth import get_user_model
# Create your models here.

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("details.html", args=[str(self.id)])

    class Meta:
        ordering = ["name"]
        verbose_name = "category"
        verbose_name_plural = "categories"


class Tour(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to="tours")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("tours", args=[str(self.id)])


class Hotel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to="hotels")
    max_room_capacity = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    current_room_capacity = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    star_rating = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("details.html", args=[str(self.id)])


class Destination(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to="locations")

    def __str__(self):
        return self.country

    def get_absolute_url(self):
        return reverse("details.html", args=[str(self.id)])


class Package(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, blank=True, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=True, null=True)
    arrival_date = models.DateTimeField(blank=True, null=True)
    leaving_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ["destination"]
      
    def __str__(self):
        return self.country
    
    def get_absolute_url(self):
        return reverse("details.html", args=[str(self.id)])







    

