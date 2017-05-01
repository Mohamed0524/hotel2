from django.conf.urls import url
from HotelApp import views

app_name = 'HotelApp'
urlpatterns = [
     url(r'^$', views.hotelindex, name='hotelindex'),
     url(r'^hotels/(?P<pk>[0-9]+)/$', views.hoteldetails, name='hoteldetails'),
     url(r'^(?P<id>[0-9]+)/reviews/create$', views.reviewCreateView.as_view(), name='createreview'),
     url(r'^(?P<pk>[0-9]+)/reviews/edit$', views.reviewUpdateView.as_view(), name='editreview'),
     url(r'^(?P<pk>[0-9]+)/reviews/delete$', views.reviewDeleteView.as_view(), name='deletereview'),
]
