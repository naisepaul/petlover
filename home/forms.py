from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

# Class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField

#     Class Meta:
#         Model = User
#         fields =['name', 'username', 'email']

# Class ProfileUpdateForm(forms.ModelForm):
#     email = forms.EmailField

#     Class Meta:
#         Model = User
#         fields =['phone', 'profile_image']    

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image','name', 'username', 'email','phone']  # Adjust fields as per your UserProfile model

