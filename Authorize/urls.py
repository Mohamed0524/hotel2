from django.conf.urls import url
from HotelApp import views
from Authorize import views
# Url patters for authorization such as accepting , deleting and removing a partner.
app_name = 'Authorize'
urlpatterns = [
         url(r'^$', views.displayDash, name='displayDash'),
         url(r'^admindash$', views.displayAdminDash, name='admindash'),
         url(r'^admindash/proposals$', views.showProposals, name='showproposals'),
         url(r'^admindash/partners$', views.showPartners, name='showpartners'),
         url(r'^admindash/partners/(?P<id>[0-9]+)/remove$', views.removePartner, name='removepartner'),
         url(r'^admindash/proposals/(?P<id>[0-9]+)/accept$', views.acceptProposals, name='acceptproposal'),
         url(r'^admindash/proposals/(?P<id>[0-9]+)/decline$', views.declineProposals, name='declineproposal'),
         url(r'^partner/checkstatus$', views.checkstatus, name='checkproposal'),
]
