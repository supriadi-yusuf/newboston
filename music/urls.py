from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^music/', include('music.urls')),
    url(r'^$', views.albumList, name='album_list'),
    url(r'^(?P<album_id>\d+)/$', views.albumDetail, name='album_detail'),

]
