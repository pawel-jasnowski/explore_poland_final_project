import django_filters
from .models import Places

class PlacesFilter(django_filters.FilterSet):

    class Meta:
        model = Places
        fields = [
            'region',
            'city',
            'price_per_night',
        ]


