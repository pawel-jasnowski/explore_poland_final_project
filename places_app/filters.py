import django_filters
from .models import Places
from distutils.util import strtobool


REGION = {
    ("Sea", "Sea"),
    ("Mountains", "Mountains"),
    ("Lakes", "Lakes")
}

class PlacesFilter(django_filters.FilterSet):
    place_name = django_filters.CharFilter(lookup_expr='iexact')
    # region = django_filters.TypedChoiceFilter(choices=REGION,
    #                                         coerce=strtobool)
    class Meta:
        model = Places
        fields = ['region', 'object_type']
