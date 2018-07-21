from django.db import models

# Create your models here.
Class Album( models.Model):
    artis = models.CharField(max-length=250)
    title = models.CharField(max-length=500)
    genre = models.CharField(max-length=100)
    logo = models.CharField(max-length=1000)

Class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max-length=10)
    title = models.CharField(max-length=250)
