import django_filters
from multiselectfield import MultiSelectField

from .models import Places, FACILITIES_CHOICES
from distutils.util import strtobool


REGION = {
    ("Sea", "Sea"),
    ("Mountains", "Mountains"),
    ("Lakes", "Lakes")
}

class PlacesFilter(django_filters.FilterSet):
    place_name = django_filters.CharFilter(lookup_expr='iexact')
    facilities = MultiSelectField(choices=FACILITIES_CHOICES, max_choices=10, max_length=100, blank=False, null=False,
                                  default='')
    class Meta:
        model = Places
        fields = ['object_type']
        filter_overrides = {models.CharField}
