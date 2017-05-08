from django import forms
from ManageHotels.models import Photo

# Using djangos Model forms to create a form using a model.
class PhotoForm(forms.ModelForm):
 class Meta:
     model = Photo
     fields = ['path',]
