from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from Authorize.models import Partners
# Stores all the hotel details and is used to query hotels.
class Hotels(models.Model):
    Name = models.CharField(max_length  = 255)
    Address = models.CharField(max_length  = 255)
    City = models.CharField(max_length  = 255)
    Country = models.CharField(max_length  = 255)
    TelephoneNumber = models.CharField(max_length=12)
    ImagePath = models.CharField(max_length  = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)
    Description = models.TextField(max_length  = 140)
    Partner = models.ForeignKey(Partners,on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Hotels'

    def get_absolute_url(self):
        return reverse('hoteldetails', kwargs={'pk': self.pk})
    def __str__(self):
         return self.Name
# Stores the Hotel reviews and is used to query the reviews
class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE)
    comment = models.CharField(max_length  = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(default = 0)
    class Meta:
        verbose_name_plural = 'Review'

    def __str__(self):
         return self.comment
# Stores the Hotels rooms
class Room(models.Model):
    hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE)
    RoomType = models.CharField(max_length  = 255)
    Capacity = models.IntegerField(default = 0)
    BedOption = models.CharField(max_length  = 255)
    Price= models.IntegerField(default = 0)
    View = models.CharField(max_length  = 255)
    TotalRooms = models.CharField(max_length  = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'Room'

    def __str__(self):
         return self.RoomType
# Stores and is used to query partner proposals
class Proposal(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    CompanyName = models.CharField(max_length  = 255)
    CompanyEmail = models.EmailField(max_length  = 254)
    HQAddress = models.CharField(max_length  = 255)
    Vision = models.TextField(max_length  = 400)
    class Meta:
        verbose_name_plural = 'Proposal'

    def __str__(self):
         return self.CompanyName
