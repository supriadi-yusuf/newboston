from django.conf.urls import url
from . import views

app_name = 'music_app' # add name space to url name for this app

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^music/', include('music.urls')),
    url(r'^$', views.index, name='album_list')

]
