from django.contrib import admin
from .models import Profile
from django_summernote.admin import SummernoteModelAdmin

# register the models here

admin.site.register(Profile)



# register the Dog in the admin pannel

# @admin.register(Dog)

# # class DogAdmin(SummernoteModelAdmin):
#     summernote_fields = ('description')
