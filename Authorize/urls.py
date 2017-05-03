from django.conf.urls import url
from HotelApp import views
from Authorize import views

app_name = 'Authorize'
urlpatterns = [
         url(r'^$', views.displayDash, name='displayDash'),
]
