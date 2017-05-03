from django.shortcuts import render
from django.http import HttpResponse
from Authorize.models import Role,UserRole
from django.core.urlresolvers import reverse,reverse_lazy
from django.http import HttpResponse,HttpResponseRedirect

def displayDash(request):
    user = request.user
    if user.userrole.roleid == 3:
        link = reverse('HotelApp:hotelindex')
        return HttpResponseRedirect(link)
    elif user.userrole.roleid == 4:
            link = reverse('ManageHotels:home')
            return HttpResponseRedirect(link)
