from django.contrib import admin
from .models import Places

@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    fields =  ["place_name", "city", "region", "object_type", "facilities", "price_per_night", "description", "images"]
    list_display = ["place_name", "city", "region", "object_type", "price_per_night"]
    list_filter = ("region", )
    search_fields = ("place_name", "city", "region", "object_type", "facilities")

# Register your models here.
