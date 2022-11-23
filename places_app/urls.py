from django.urls import path
from places_app.views import all_places, new_place, edit_place, delete_place

urlpatterns = [
    path('places/', all_places, name='all_places'),
    path('new/', new_place, name='new_place'),
    path('edit/<int:id>/', edit_place, name='edit_place'),
    path('delete/<int:id>/', delete_place, name='delete_place')
]