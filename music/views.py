from django.shortcuts import render, get_object_or_404
from .models import Album

# view is simple function/class that returns html
def albumList(request):
    all_albums = Album.objects.all()
    context = { 'all_albums' : all_albums }
    return render( request, 'music/album_list.html', context)

def albumDetail(request, album_id):
    # album = Album.objects.get(pk=album_id)
    album = get_object_or_404( Album, pk=album_id)
    return render( request, 'music/album_detail.html', { 'album':album})
