from django.db import models
from django.contrib.auth.models import User
# from django_resized import ResizedImageField
from cloudinary.models import CloudinaryField
import uuid

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True)
    username = models.CharField(max_length=200, blank=False, null=True)
    name = models.CharField(max_length=200, blank=False, null=True)
    email = models.EmailField(max_length=300, blank=False, null=True)  
    phone = models.CharField(max_length=100, blank=True, null=True)  
    # profile_image = models.ImageField(
    #     upload_to='user_photos/', blank=True,
    #     null=True)
    profile_image = CloudinaryField('image', default='https://res.cloudinary.com/dmhdrvehj/image/upload/v1709854103/user_photos/default-user-image_jjhzic.webp')
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          editable=False, primary_key=True)

    # def __str__(self):
    #     return f'{self.user.username} Profile'                         
    def __str__(self):
        return str(self.username)

    @property
    def profile_img(self):
        if self.profile_image:
            url = self.profile_image.url
        else:
            url = (
                'https://res.cloudinary.com/dmhdrvehj/image/upload/v1709854103/user_photos/default-user-image_jjhzic.webp'
            )
        return url

# class Dog(models.Model):
#     SEX_CHOICES = [
#         ('M', 'Male'),
#         ('F', 'Female'),     
#     ]

    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # breed = models.CharField(max_length=100)
    # # date_of_birth = models.DateField()
    # sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='M')
    # description = models.TextField(null=True, blank=True)

    # def __str__(self):
    #     return self.breed

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