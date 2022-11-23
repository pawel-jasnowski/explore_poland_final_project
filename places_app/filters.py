import django_filters
from .models import Places


REGION = {
    ("Sea", "Sea"),
    ("Mountains", "Mountains"),
    ("Lakes", "Lakes")
}

class PlacesFilter(django_filters.FilterSet):
    class Meta:
        model = Places
        fields = {
            'region'
        }
