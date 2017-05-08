from django.conf.urls import url
from Reservations import views
from Reservations.views import GeneratePDF

# Sets the namespace that can be referred to throughout the django project.
app_name = 'Reservations'
#Urls in regular expression format trigger a view when a url is matched.
urlpatterns = [

    url(r'^book/(?P<hotelid>[0-9]+)/(?P<roomid>[0-9]+)$', views.bookRoom, name='bookroom'),
    url(r"^book/new/(?P<roomid>[0-9]+)/(?P<hotelid>[0-9]+)/(?P<checkin>(\d{4}-\d{2}-\d{2}))/(?P<checkout>(\d{4}-\d{2}-\d{2}))/(?P<totalcost>[0-9]+)$"
    , views.storeBooking, name='newbooking'),
    url(r'^mybookings/$', views.mybookings, name='viewbookings'),
    url(r'^mybookings/cancel/(?P<id>[0-9]+)$', views.cancelbooking, name='cancelbooking'),
    url(r'^mybookings/(?P<id>[0-9]+)/pdf$', GeneratePDF.as_view(), name='gpdf'),

]
