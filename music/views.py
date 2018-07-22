from django.http import HttpResponse
from django.shortcuts import render
from .models import Album

# view is simple function/class that returns html
def albumList(request):
    all_albums = Album.objects.all()
    context = { 'all_albums' : all_albums }
    return render( request, 'music/album_list.html', context)

def albumDetail(request, album_id):
    return HttpResponse("<h1>Detail for music with id=" + str(album_id) + "</h1>")
