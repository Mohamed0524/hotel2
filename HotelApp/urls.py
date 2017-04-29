from django.conf.urls import url
from HotelApp import views

app_name = 'HotelApp'
urlpatterns = [
     url(r'^$', views.hotelindex, name='hotelindex'),
     url(r'^hotels/(?P<pk>[0-9]+)/$', views.HotelDetailView.as_view(), name='hoteldetails'),
]
