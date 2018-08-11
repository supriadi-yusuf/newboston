from django.conf.urls import url
from . import views

# spd - since we use rest_framework we need this
#from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'rest_api_app'

urlpatterns = [

    # spd - stocklist/
    url(r'^stocklist/$',views.StockListView.as_view(), name='stock-list'),

    # spd - stocklist/pk
    url(r'^stocklist/(?P<pk>\d+)/$', views.StockView.as_view(), name='stock'),

]

# spd - for rest_framework
#urlpatterns = format_suffix_patterns(urlpatterns)
