from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from HotelApp.models import Hotels
from django.views import generic
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'HotelApp/home.html')
@login_required
def hotelindex(request):
    hotels_list = Hotels.objects.all()
    context = {'Hotels': hotels_list}
    return render(request,'HotelApp/showhotels.html',context)

class HotelDetailView(generic.DetailView):
    model = Hotels
    template_name = 'HotelApp/hoteldetails.html'
