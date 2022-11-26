import django_filters
from django_filters import ChoiceFilter
from multiselectfield import MultiSelectField
from django import forms
from .models import Places
from distutils.util import strtobool

FACILITIES_CHOICES = ((1, 'Swimming pool'), (2, 'Free parking outside'), (3, 'Wi-Fi'), (4, 'Pet friendly'), (5, 'SPA'),
                      (6, 'Private kitchen'), (7, 'Bike rating'), (8, 'BBQ Place'), (9, 'coffee maker'), (10, 'family room'))


# class PlacesFilter(django_filters.FilterSet):
#     place_name = django_filters.CharFilter(lookup_expr='iexact')
#     facilities = django_filters.ModelChoiceFilter(field_name='facilities', lookup_expr='isnull',null_label='Uncategorized',queryset=Facilities.objects.all(),)
#     class Meta:
#         model = Places
#         fields = ['object_type']

class PlacesFilter(django_filters.FilterSet):
    facilities = django_filters.MultipleChoiceFilter(choices=Places.FacilitiesChoices.choices, widget=forms.CheckboxSelectMultiple())
    price_per_night = django_filters.RangeFilter()
    class Meta:
        model = Places
        fields = ['facilities', 'price_per_night']

