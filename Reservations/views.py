from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from HotelApp.models import Hotels
from HotelApp.models import Room
from django import forms
from django.core.urlresolvers import reverse,reverse_lazy
from ManageHotels.models import Photo
from HotelApp.models import Proposal
from django.core.urlresolvers import reverse
from django.views import View
from django.db.models import Q
from django.core.signing import Signer
import datetime
from Reservations.models import Reservation
# Create your views here.
def bookRoom(request,hotelid,roomid):
    FirstDate = request.session['checkin']
    SecDate =  request.session['checkout']

    Checkin = datetime.datetime.strptime(FirstDate, "%Y-%m-%d").date()
    Checkout = datetime.datetime.strptime(SecDate, "%Y-%m-%d").date()
    timedeltaSum = Checkout - Checkin
    StayDuration = timedeltaSum.days

    del request.session['checkin']
    del request.session['checkout']

    Hotel = Hotels.objects.get(id= hotelid)
    theRoom = Room.objects.get(id = roomid)

    price = theRoom.Price
    TotalCost = StayDuration * price


    context = {'checkin': Checkin, 'checkout':Checkout,'stayduration':StayDuration,'hotel':Hotel,'room':theRoom,'price':price,
    'totalcost':TotalCost}
    return render(request, 'Reservations/booking.html', context)

def storeBooking(request,hotelid,roomid,checkin,checkout,totalcost):
    if request.method == 'POST':

        Firstname = request.POST.get('firstname')
        Lastname = request.POST.get('lastname')
        user = request.user
        hotel = Hotels.objects.get(id = hotelid)
        room = Room.objects.get(id = roomid)
        cost = totalcost
        newReservation = Reservation()
        newReservation.hotel = hotel
        newReservation.room = room
        newReservation.user = user
        newReservation.guestFirstName = Firstname
        newReservation.guestLastName = Lastname
        newReservation.CheckIn = checkin
        newReservation.CheckOut = checkout
        newReservation.totalPrice = cost
        newReservation.save()
        link = reverse('HotelApp:userDash')
        return HttpResponseRedirect(link)

    else:
        url = reverse('HotelApp:userDash')
        return url
