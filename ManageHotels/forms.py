from django import forms
from ManageHotels.models import Photo


class PhotoForm(forms.ModelForm):
 class Meta:
     model = Photo
     fields = ['path',]
