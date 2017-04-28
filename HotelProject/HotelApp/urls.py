from django.conf.urls import url
from HotelApp import views

urlpatterns = [
     url(r'^$', views.hotelindex, name='hotelindex'),
]
