from django.contrib import admin
from HotelApp.models import Hotels
from HotelApp.models import Review
# Registers the Hotels and review models on the Django Admin page
admin.site.register(Hotels)
admin.site.register(Review)
