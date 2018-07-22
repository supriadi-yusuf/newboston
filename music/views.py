from django.http import HttpResponse
from django.template import loader
from .models import Album
#from django.shortcuts import render

# view is simple function/class that returns html
def albumList(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/album_list.html')
    context = {
        'all_albums' : all_albums,
    }

    return HttpResponse(template.render(context,request))

def albumDetail(request, album_id):
    return HttpResponse("<h1>Detail for music with id=" + str(album_id) + "</h1>")
