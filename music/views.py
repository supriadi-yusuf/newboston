from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Album, Song

class IndexView(generic.ListView): # there is no rule for class name here
    template_name = 'music/album_list.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()
    #model = Album

class DetailView(generic.DetailView): # there is no rule for class name here
    model = Album
    template_name = 'music/album_detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'title', 'genre', 'logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'title', 'genre', 'logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music_app:album-list')
