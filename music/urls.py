from django.conf.urls import url
from . import views

app_name = "music_app" # this is url name space

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^music/', include('music.urls')),
    url(r'^$', views.IndexView.as_view(), name='album_list'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='album_detail'),
    #url(r'^(?P<album_id>\d+)/favorite/$', views.songFavorite, name='song_favorite'),
    url(r'^album/add/$', views.AlbumCreate.as_view(), name='album-add'),

]
