from django.contrib import admin
from .models import Dog
from django_summernote.admin import SummernoteModelAdmin


# register the Dog in the admin pannel

@admin.register(Dog)

class DogAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')
