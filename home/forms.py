from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile, Dog, Listing

# Profile form

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image','name', 'username', 'email','phone']  

    def clean(self):
            cleaned_data = super().clean()
            username = cleaned_data.get("username")
            email = cleaned_data.get("email")
            
            # Check if the entered username already exists
            if User.objects.exclude(pk=self.instance.user_id).filter(username=username).exists():
                self.add_error('username', 'This username is already in use.')
                cleaned_data['username'] = self.instance.user.username
            
            # Check if the entered email already exists
            if User.objects.exclude(pk=self.instance.user_id).filter(email=email).exists():
                self.add_error('email', 'This email address is already in use.')
                cleaned_data['email'] = self.instance.user.email
            return cleaned_data    


# Dog Listing Form

class DogListingForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['breed', 'DOB', 'sex', 'temperament', 'photo']

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['price', 'location', 'description']

