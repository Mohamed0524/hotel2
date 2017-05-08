#Import the required Models (Usually foreing keys)
from django.db import models
from HotelApp.models import Hotels,Room
from django.contrib.auth.models import User
#Create a Reservation Model which stores booking details
class Reservation(models.Model):
    hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    guestFirstName = models.CharField(max_length  = 255)
    guestLastName = models.CharField(max_length  = 255)
    CheckIn = models.DateField()
    CheckOut = models.DateField()
    totalPrice = models.IntegerField(default = 0)

    class Meta:
        verbose_name_plural = 'Reservation'

    def __str__(self):
         return self.guestLastName
