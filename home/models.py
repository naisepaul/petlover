from django.db import models
from django.contrib.auth.models import User
# from django_resized import ResizedImageField
from cloudinary.models import CloudinaryField
import uuid
from . import choice

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True)
    username = models.CharField(max_length=200, blank=False, null=True)
    name = models.CharField(max_length=200, blank=False, null=True)
    email = models.EmailField(max_length=300, blank=False, null=True)  
    phone = models.CharField(max_length=100, blank=True, null=True)  
    profile_image = CloudinaryField('image', default = "https://res.cloudinary.com/dmhdrvehj/image/upload/v1709854103/user_photos/default-user-image_jjhzic.webp")
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          editable=False, primary_key=True)
                        
    def __str__(self):
        return str(self.username)

class Dog(models.Model):   
    
    breed = models.CharField(max_length=100, choices = choice.DOG_BREED)
    DOB = models.DateField()  # Date of Birth
    sex = models.CharField(max_length=1, choices=choice.SEX_CHOICES)
    temperament = models.TextField(max_length=100, choices = choice.TEMPERAMENT)  
    owner = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)  
    photo = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)       

    def __str__(self):
        return f"{self.breed} ({self.sex}), DOB: {self.DOB}"

class Listing(models.Model):
    
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100, choices=choice.COUNTIES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,null=False)
    # id = models.UUIDField(default=uuid.uuid4, unique=True,
    #                       primary_key=True, editable=False)
    
    def __str__(self):
         return f"Listing for {self.dog.breed} - {self.location}"