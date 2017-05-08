import datetime
from django.db.models import Sum
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.core.urlresolvers import reverse,reverse_lazy
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from django import forms
from HotelApp.models import Hotels,Review,Room
from ManageHotels.forms import PhotoForm
from ManageHotels.models import Photo
from django.views import generic,View
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.template import RequestContext
from Authorize.models import Partners
from Reservations.models import Reservation



# Show the Partner Homepage if the request is made by a partner.
def home(request):
    user = request.user
    partner = user.partners
    PartnerHotel = Hotels.objects.filter(Partner_id = partner.id).count()
    print (partner.id)
    if partner:
            context = {'Partner': partner,'NumHotel':PartnerHotel}
            return render(request,'ManageHotels/home.html',context)

    else:
        return HttpResponse("Error")

# Show the partner their hotels.
@login_required
def showhotels(request):
    user = request.user
    thepartner= Partners.objects.get(userID = user)
    hotels_list = Hotels.objects.filter(Partner=thepartner)
    context = {'Hotels': hotels_list}
    return render(request,'ManageHotels/yourhotels.html',context)

#Show the partner reservations for specific hotels.
def showreservations(request,pk):
    thehotel = Hotels.objects.get(id = pk)
    Bookings = Reservation.objects.filter(hotel= thehotel)
    context = {'reservations':Bookings,'hotel':thehotel}
    return render(request,'ManageHotels/viewbookings.html',context)

# Display a hotel dashboard enabling the partner to manage their hotels including add rooms
def showdashboard(request,pk):
    thehotel = Hotels.objects.get(id = pk)
    context = {'Hotel': thehotel}
    return render(request,'ManageHotels/hoteldash.html',context)


def managehotel(request,pk):
    thehotel = Hotels.objects.get(id = pk)
    context = {'Hotel': thehotel}
    return render(request,'ManageHotels/managehotel.html',context)

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
        thehotel = Hotels.objects.get(id = id)
        photos = Photo.objects.filter(hotel =thehotel)
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
# Generate Create Update and delete views using django's Createview
class HotelCreateView(CreateView):

    model = Hotels
    fields = ['Name','Address','City','Country','TelephoneNumber','Description']
    def get_success_url(self):
        #hotelid = self.kwargs['id']
        #url = reverse('HotelApp:hoteldetails', args=[hotelid])
        url = reverse('ManageHotels:home')
        return url
    def form_valid(self, form):
        user = self.request.user
        thepartner= Partners.objects.get(userID = user)
        form.instance.Partner_id = thepartner.id
        return super(HotelCreateView, self).form_valid(form)
class HotelUpdateView(UpdateView):

    model = Hotels
    fields = ['Name','Address','City','Country','TelephoneNumber','Description']
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
    fields = ['RoomType','Capacity','BedOption','Price','View','TotalRooms']
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

# use a django defined view to show the image upload.
#This view also handles post retrieving and returning a json response.
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

class ChartView(View):
    def get(self,request,id):
        return render(request, 'ManageHotels/PartnerCharts.html')

#Using django rest to send data to he views.
class ChartData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request,id, format=None):
        # Loads the hotel countires with a list of countries within which the partner operates
        # Get the number of Hotels in each country.
        HotelCountries = Hotels.objects.filter(Partner_id = id).values_list('Country', flat = True).distinct()
        count = []
        for Country in HotelCountries:
            count.append(Hotels.objects.filter(Country = Country).count())

        # Get the number of bookings made by each hotel
        HotelNames = Hotels.objects.filter(Partner_id = id).values_list('Name', flat = True)
        PartnerHotel = Hotels.objects.filter(Partner_id = id)
        bookings = []
        # calculate the amount of money each hotel has made this year.
        for Hotel in PartnerHotel:
            bookings.append(Reservation.objects.filter(hotel = Hotel).count())

        today = datetime.datetime.now()
        money = []
        for Hotel in PartnerHotel:

            money.append(Reservation.objects.filter(hotel = Hotel ,CheckOut__year = today.year).aggregate(sum=Sum('totalPrice'))['sum'])


        data = {"Countries":HotelCountries,"Count":count,"Hotels":HotelNames,"Bookings":bookings,"Money":money}
        print(PartnerHotel)
        return Response(data)
# Partners can cancel a booking made by a user.
def cancelbooking(request,pk):
    Booking = Reservation.objects.get(id = pk)
    hotelid = Booking.hotel.id
    Booking.delete()
    link = reverse('ManageHotels:hotelreservations', args=[hotelid])
    return HttpResponseRedirect(link)
