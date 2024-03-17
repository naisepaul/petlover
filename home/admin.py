from django.contrib import admin
from .models import Profile, Dog, Listing
from django_summernote.admin import SummernoteModelAdmin

# register the models here

admin.site.register(Profile)
admin.site.register(Dog)
admin.site.register(Listing)




# # class DogAdmin(SummernoteModelAdmin):
#     summernote_fields = ('description')
