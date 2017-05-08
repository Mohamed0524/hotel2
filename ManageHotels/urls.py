from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from ManageHotels import views
from ManageHotels.views import ChartData,ChartView

app_name = 'ManageHotels'

# Specifying all the urls for the Manage Hotels app which the partners will see .
# Allows for Creating Hotels , Editing them and photos , and adding rooms etc.
urlpatterns = [
     url(r'^$', views.home, name='home'),
     url(r'^newhotel$', views.HotelCreateView.as_view(), name='createhotel'),
     url(r'^yourhotels$', views.showhotels, name='showhotel'),
     url(r'^yourhotels/(?P<pk>[0-9]+)/edit$', views.HotelUpdateView.as_view(), name='editHotel'),
     url(r'^yourhotels/(?P<pk>[0-9]+)/bookings$', views.showreservations, name='hotelreservations'),
     url(r'^yourhotels/(?P<pk>[0-9]+)/delete$', views.HotelDeleteView.as_view(), name='deleteHotel'),
     url(r'^yourhotels/bookings/(?P<pk>[0-9]+)/delete$', views.cancelbooking, name='removebooking'),
     url(r'^yourhotels/(?P<pk>[0-9]+)/dashboard$', views.showdashboard, name='hoteldash'),
     url(r'^yourhotels/(?P<pk>[0-9]+)/manage$', views.managehotel, name='managehotel'),
     url(r'^yourhotels/(?P<pk>[0-9]+)/rooms$', views.showRoomsDash, name='showRoomsDash'),
     url(r'^yourhotels/(?P<pk>[0-9]+)/rooms/add$', views.RoomCreateView.as_view(), name='addRoom'),
     url(r'^yourhotels/(?P<pk>[0-9]+)/rooms/edit$', views.RoomUpdateView.as_view(), name='editRoom'),
     url(r'^yourhotels/(?P<pk>[0-9]+)/rooms/delete$', views.RoomDeleteView.as_view(), name='deleteRoom'),
     url(r'^yourhotels/(?P<id>[0-9]+)/upload$', views.BasicUploadView.as_view(), name='basicupload'),
     url(r'^yourhotels/(?P<id>[0-9]+)/photodash$', views.showphotodash, name='photodash'),
     url(r'^yourhotels/(?P<id>[0-9]+)/thumbnail$', views.editThumbnail, name='editThumb'),
     url(r'^yourhotels/(?P<id>[0-9]+)/deletephoto$', views.deletePhoto, name='deletephoto'),
     url(r'^yourhotels/(?P<id>[0-9]+)/charts$', ChartView.as_view(), name = 'partnercharts'),
     url(r'^yourhotels/(?P<id>[0-9]+)/chart/data$', ChartData.as_view()),


]
