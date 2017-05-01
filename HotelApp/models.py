from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
class Hotels(models.Model):
    Name = models.CharField(max_length  = 255)
    Address = models.CharField(max_length  = 255)
    City = models.CharField(max_length  = 255)
    Country = models.CharField(max_length  = 255)
    TelephoneNumber = models.IntegerField(default = 0)
    ImagePath = models.CharField(max_length  = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)
    Description = models.CharField(max_length  = 255)
    class Meta:
        verbose_name_plural = 'Hotels'

    def get_absolute_url(self):
        return reverse('hoteldetails', kwargs={'pk': self.pk})
    def __str__(self):
         return self.Name

class Review(models.Model):
    user = models.ForeignKey(User)
    hotel = models.ForeignKey(Hotels)
    comment = models.CharField(max_length  = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(default = 0)
    class Meta:
        verbose_name_plural = 'Review'

    def __str__(self):
         return self.comment
