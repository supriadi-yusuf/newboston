from django.conf.urls import url
from . import views

app_name = "music_app" # this is url name space

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^music/', include('music.urls')),

    # /music/
    url(r'^$', views.IndexView.as_view(), name='album-list'),

    # /music/2/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='album-detail'),
    #url(r'^(?P<album_id>\d+)/favorite/$', views.songFavorite, name='song_favorite'),

    # /music/add/
    url(r'^add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /music/2/update/
    url(r'^(?P<pk>\d+)/update/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/2/delete/
    url(r'^(?P<pk>\d+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

]
