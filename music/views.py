from django.views import generic
from .models import Album, Song

class IndexView(generic.ListView): # there is no rule for class name here
    template_name = 'music/album_list.html'

    def get_queryset(self):
        return Album.objects.all()
    #model = Album

class DetailView(generic.DetailView): # there is no rule for class name here
    model = Album
    template_name = 'music/album_detail.html'
