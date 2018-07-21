from django.contrib import admin

from .models import Album, Song

# Register your models here, so it can be accessed via admin page
admin.site.register(Album) # register Album model
admin.site.register(Song) # register Song model
