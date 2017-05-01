from django.conf.urls import url
from ManageHotels import views

app_name = 'ManageHotels'
urlpatterns = [
     url(r'^$', views.home, name='home'),
     url(r'^newhotel$', views.HotelCreateView.as_view(), name='createhotel'),
     url(r'^yourhotels$', views.showhotels, name='showhotel'),
     url(r'^yourhotels/(?P<pk>[0-9]+)/dashboard$', views.showdashboard, name='showHotelDash'),
     url(r'^yourhotels/(?P<pk>[0-9]+)/rooms$', views.showRoomsDash, name='showRoomsDash'),
     url(r'^yourhotels/(?P<pk>[0-9]+)/rooms/add$', views.RoomCreateView.as_view(), name='addRoom'),
    
]
