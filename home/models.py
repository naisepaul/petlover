from django.db import models
from django.contrib.auth.models import User
# from django_resized import ResizedImageField
from cloudinary.models import CloudinaryField
import uuid

# Create your models here.

class Dog(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),     
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    breed = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='M')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.breed

# class Listing(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
#     owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     created = models.DateTimeField(auto_now_add=True)
#     description = models.TextField(null=True, blank=True)
#     listing_image_1 = ResizedImageField(
#         quality=75, force_format='WEBP', blank=True,
#         upload_to='listings/', default='listings/default-listing-img.jpg')
#     def __str__(self):
#         return f"Listing for {self.dog.name} by {self.owner.name}"


# def __str__(self):
#         return str(self.dog_breed)