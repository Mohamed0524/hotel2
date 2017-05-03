from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from HotelApp.models import Hotels

class Photo(models.Model):

    path = models.FileField()
    hotel = models.ForeignKey(Hotels)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'Photo'

    def __str__(self):
         return self.path
