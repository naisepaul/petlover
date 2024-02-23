from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import uuid

# Create your models here.

class Dog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name

class Owner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    town = models.CharField(max_length=100)
    password = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    listing_image_1 = ResizedImageField(
        quality=75, force_format='WEBP', blank=True,
        upload_to='listings/', default='listings/default-listing-img.jpg')
    def __str__(self):
        return f"Listing for {self.dog.name} by {self.owner.name}"


def __str__(self):
        return str(self.dog_breed)