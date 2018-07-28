from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=250)
    title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    logo = models.CharField(max_length=1000)

    #whenever data is inserted then run this function
    def get_absolute_url(self):
        # take to url named as 'music_app:album_detail' with some pamaeters (kwargs)
        return reverse('music_app:album-detail', kwargs={'pk': self.pk})

    def __str__(self): # string representation of object
        return self.artist + " - " + self.title

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title
