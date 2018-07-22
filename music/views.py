from django.http import HttpResponse
from .models import Album
#from django.shortcuts import render

# view is simple function/class that returns html
def albumList(request):
    html = ''

    all_albums = Album.objects.all()
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href="' + url + '">' + album.title + '</a><br>'

    return HttpResponse(html)

def albumDetail(request, album_id):
    return HttpResponse("<h1>Detail for music with id=" + str(album_id) + "</h1>")
