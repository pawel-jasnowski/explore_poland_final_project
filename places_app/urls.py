from django.urls import path
from places_app.views import all_places


urlpatterns = [
    path('places/', all_places)
]