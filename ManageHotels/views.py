from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response
from HotelApp.models import Hotels
from HotelApp.models import Review
from HotelApp.models import Room
from django.views import generic
from django.contrib.auth.decorators import login_required
from django import forms
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse,reverse_lazy
from django.template import RequestContext
from ManageHotels.forms import PhotoForm
from ManageHotels.models import Photo
from django.http import JsonResponse
from django.views import View
from django.core.files.storage import FileSystemStorage


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

def showphotodash(request,id):
    thehotel = Hotels.objects.get(id = id)
    photos = Photo.objects.filter(hotel =thehotel)
    thumbnail = photos.first()
    context = {'Hotel': thehotel,'Photos':photos,'Thumbnail':thumbnail}
    return render(request,'ManageHotels/photoDash.html',context)
def editThumbnail(request,id):
    if request.method == 'POST' and request.FILES['thumb']:
        thumb = request.FILES['thumb']
        fs = FileSystemStorage()
        filename = fs.save(thumb.name,thumb)
        name = thumb.name
        photos = Photo.objects.all()
        thumbnail = photos.first()
        thumbnail.path = name
        thumbnail.save()
        link = reverse('ManageHotels:photodash', args=[id])
        return HttpResponseRedirect(link)
def deletePhoto(request,id):
       photo = Photo.objects.get(id = id)
       hotel = photo.hotel
       photo.delete()
       link = reverse('ManageHotels:photodash', args=[hotel.id])
       return HttpResponseRedirect(link)

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
class HotelUpdateView(UpdateView):

    model = Hotels
    fields = ['Name','Address','City','Country','TelephoneNumber','ImagePath','Description']
    def get_success_url(self):
        hotelid = self.kwargs['pk']
        url = reverse('ManageHotels:photodash', args=[hotelid])
        return url
    def form_valid(self, form):
        return super(UpdateView, self).form_valid(form)

class HotelDeleteView(DeleteView):
    model = Hotels
    def get_success_url(self):
        url = reverse('ManageHotels:home')
        return url
    def form_valid(self, form):
        return super(HotelDeleteView, self).form_valid(form)

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
        return super(RoomUpdateView, self).form_valid(form)


class RoomDeleteView(DeleteView):

    model = Room
    def get_success_url(self):
        roomid = self.kwargs['pk']
        room= Room.objects.get(id = roomid)
        hotel = room.hotel
        hotelid = hotel.id
        url = reverse('ManageHotels:showRoomsDash', args=[hotelid])
        return url

class BasicUploadView(View):
    def get(self,request,id):
        photos_list = Photo.objects.filter(hotel=id)
        return render(self.request, 'ManageHotels/uploadf.html',{'photos':photos_list,'hotelid':id})
    def post(self,request,id):

        form = PhotoForm(self.request.POST,self.request.FILES)


        if form.is_valid():
            photo = form.save(commit=False)
            hotel = Hotels.objects.get(id = id)
            photo.hotel = hotel
            photo.save()
            data = {'is_valid':True,'name':photo.path.name, 'url':photo.path.url}
        else:
            data = {is_valid:False}
        return JsonResponse(data)
