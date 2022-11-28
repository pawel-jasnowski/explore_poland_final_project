from django.contrib import admin
from .models import Places, PlacesImage

class PlacesImageAdmin(admin.StackedInline):
    model = PlacesImage
@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    inlines = [PlacesImageAdmin]
    fields =  ["place_name", "city", "region", "object_type", "facilities", "price_per_night", "description", "images"]
    list_display = ["place_name", "city", "region", "object_type", "price_per_night"]
    list_filter = ("region", )
    search_fields = ("place_name", "city", "region", "object_type", "facilities")

    class Meta:
        model = Places

@admin.register(PlacesImage)
class PlacesImageAdmin(admin.ModelAdmin):
    pass

# Register your models here.
