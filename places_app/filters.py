import django_filters
from django_filters import ChoiceFilter
from django import forms
from multiselectfield import MultiSelectField
from distutils.util import strtobool

from .models import Places


FACILITIES_CHOICES = ((1, 'Swimming pool'), (2, 'Free parking outside'), (3, 'Wi-Fi'), (4, 'Pet friendly'), (5, 'SPA'),
                      (6, 'Private kitchen'), (7, 'Bike rating'), (8, 'BBQ Place'), (9, 'coffee maker'), (10, 'family room'))


class PlacesFilter(django_filters.FilterSet):
    place_name = django_filters.CharFilter(lookup_expr='iexact')
    facilities = django_filters.ChoiceFilter(choices=FACILITIES_CHOICES)
    price_per_night = django_filters.RangeFilter(lookup_expr='iexact')
    class Meta:
        model = Places
        fields = ['object_type', 'price_per_night', 'facilities']


# class PlacesFilter(django_filters.FilterSet):
#     facilities = django_filters.MultipleChoiceFilter(choices=Places.objects.all(), widget=forms.CheckboxSelectMultiple())
#     price_per_night = django_filters.RangeFilter()
#     class Meta:
#         model = Places
#         fields = ['facilities', 'price_per_night']

