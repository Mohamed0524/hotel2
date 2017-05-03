from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from HotelApp import views
from registration.backends.simple.views import RegistrationView
from HotelProject import settings

class MyRegistrationView(RegistrationView):
    def get_sucess_url(self,user):
        return '/'

urlpatterns = [
    url(r'^$', views.home , name = 'home'),
    url(r'^HotelApp/', include('HotelApp.urls')),
    url(r'^ManageHotels/', include('ManageHotels.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(),),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
