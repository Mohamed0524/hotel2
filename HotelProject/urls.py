from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from HotelApp import views

urlpatterns = [
    url(r'^$', views.home , name = 'home'), 
    url(r'^HotelApp/', include('HotelApp.urls')),
    url(r'^admin/', admin.site.urls),

]
