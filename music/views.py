from django.http import Http404
from django.shortcuts import render
from .models import Album

# view is simple function/class that returns html
def albumList(request):
    all_albums = Album.objects.all()
    context = { 'all_albums' : all_albums }
    return render( request, 'music/album_list.html', context)

def albumDetail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404('Album does not exist')

    return render( request, 'music/album_detail.html', { 'album':album})
