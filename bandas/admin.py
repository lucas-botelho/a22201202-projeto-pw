
# Register your models here.
from django.contrib import admin
from .models import Band, Album, Song  # Replace with your model names

admin.site.register(Band)
admin.site.register(Album)
admin.site.register(Song)