from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'HotelApp/home.html')
def hotelindex(request):
    return render(request,'HotelApp/showhotels.html')
