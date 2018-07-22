from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=250)
    title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    logo = models.CharField(max_length=1000)

    def __str__(self): # string representation of object
        return self.artist + " - " + self.title

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title
