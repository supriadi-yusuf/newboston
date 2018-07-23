from django.shortcuts import render, get_object_or_404
from .models import Album, Song

# view is simple function/class that returns html
def albumList(request):
    all_albums = Album.objects.all()
    context = { 'all_albums' : all_albums }
    return render( request, 'music/album_list.html', context)

def albumDetail(request, album_id):
    # album = Album.objects.get(pk=album_id)
    album = get_object_or_404( Album, pk=album_id)
    return render( request, 'music/album_detail.html', { 'album':album})

def songFavorite( request, album_id):
    album = get_object_or_404( Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except ( KeyError, Song.DoesNotExist):
        return render( request, 'music/album_detail.html',
                        { 'album':album,
                          'error_message': 'You did not select a valid song'
                        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render( request, 'music/album_detail.html', { 'album':album})
