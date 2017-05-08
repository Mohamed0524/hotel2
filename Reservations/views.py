import datetime
from django import forms
from django.shortcuts import render
from django.core.urlresolvers import reverse,reverse_lazy
from django.core.signing import Signer
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Q
from HotelApp.models import Hotels,Room,Proposal
from Authorize.models import UserRole
from ManageHotels.models import Photo
from Reservations.models import Reservation

from django.views import View
from django.template.loader import get_template
from .utils import render_to_pdf

## Generates a PDF using the render help function and outputs it as invoice.html
class GeneratePDF(View):
    def get(self,request, *args, **kwargs):
        booking = Reservation.objects.get(id= self.kwargs['id'])
        template = get_template('invoice.html')
        context = {"booking":booking}
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        return HttpResponse(pdf,content_type='application/pdf')



## Works out how long the user is staying in a hotel for also working out the total cost.
def bookRoom(request,hotelid,roomid):

    FirstDate = request.session['checkin']
    SecDate =  request.session['checkout']

    Checkin = datetime.datetime.strptime(FirstDate, "%Y-%m-%d").date()
    Checkout = datetime.datetime.strptime(SecDate, "%Y-%m-%d").date()
    timedeltaSum = Checkout - Checkin

    StayDuration = timedeltaSum.days

    Hotel = Hotels.objects.get(id = hotelid)
    theRoom = Room.objects.get(id = roomid)

    price = theRoom.Price
    TotalCost = StayDuration * price


    context = {'checkin': Checkin, 'checkout':Checkout,'stayduration':StayDuration,'hotel':Hotel,'room':theRoom,'price':price,
    'totalcost':TotalCost}
    return render(request, 'Reservations/booking.html', context)

# Stores the confirmed booking  into the database
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
        #Deletes the session variables.
        del request.session['checkin']
        del request.session['checkout']
        link = reverse('HotelApp:userDash')
        return HttpResponseRedirect(link)

    else:
        url = reverse('HotelApp:userDash')
        return url

#Shows the user thier previous bookings.
def mybookings(request):
    bookings = Reservation.objects.filter(user = request.user)
    context = {'bookings':bookings}
    return render(request, 'Reservations/mybookings.html', context)


# Allows a user to cancel their previous bookings , deleting a booking onclick.
def cancelbooking(request,id):
    booking = Reservation.objects.get(id = id)
    booking.delete()
    currentuser = request.user
    Role = UserRole.objects.get(user = request.user)
    link = reverse('Reservations:viewbookings')
    return HttpResponseRedirect(link)
