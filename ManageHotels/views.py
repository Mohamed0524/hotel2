from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from HotelApp.models import Hotels
from HotelApp.models import Review
from HotelApp.models import Room
from django.views import generic
from django.contrib.auth.decorators import login_required
from django import forms
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse,reverse_lazy


def home(request):
    return render(request,'ManageHotels/home.html')

@login_required
def showhotels(request):
    hotels_list = Hotels.objects.all()
    context = {'Hotels': hotels_list}
    return render(request,'ManageHotels/yourhotels.html',context)

def showdashboard(request,pk):
    thehotel = Hotels.objects.get(id = pk)
    context = {'Hotel': thehotel}
    return render(request,'ManageHotels/hoteldash.html',context)

def showRoomsDash(request,pk):
    thehotel = Hotels.objects.get(id = pk)
    rooms = Room.objects.filter(hotel=thehotel)
    context = {'Hotel': thehotel,'rooms':rooms}
    return render(request,'ManageHotels/roomDash.html',context)

class HotelCreateView(CreateView):

    model = Hotels
    fields = ['Name','Address','City','Country','TelephoneNumber','ImagePath','Description']
    def get_success_url(self):
        #hotelid = self.kwargs['id']
        #url = reverse('HotelApp:hoteldetails', args=[hotelid])
        url = reverse('ManageHotels:home')
        return url
    def form_valid(self, form):
        return super(HotelCreateView, self).form_valid(form)

class RoomCreateView(CreateView):

    model = Room
    fields = ['RoomType','Capacity','BedOption','Price','View']
    def get_success_url(self):
        hotelid = self.kwargs['pk']
        url = reverse('ManageHotels:showRoomsDash', args=[hotelid])
        return url

    def form_valid(self, form):
        form.instance.hotel_id = self.kwargs['pk']
        return super(RoomCreateView, self).form_valid(form)
class RoomUpdateView(UpdateView):

    model = Room
    fields = ['RoomType','Capacity','BedOption','Price','View','TotalRooms']
    def get_success_url(self):
        roomid = self.kwargs['pk']
        room= Room.objects.get(id = roomid)
        hotel = room.hotel
        hotelid = hotel.id
        url = reverse('ManageHotels:showRoomsDash', args=[hotelid])
        return url

    def form_valid(self, form):
        return super(UpdateView, self).form_valid(form)


class RoomDeleteView(DeleteView):

    model = Room
    def get_success_url(self):
        roomid = self.kwargs['pk']
        room= Room.objects.get(id = roomid)
        hotel = room.hotel
        hotelid = hotel.id
        url = reverse('ManageHotels:showRoomsDash', args=[hotelid])
        return url
