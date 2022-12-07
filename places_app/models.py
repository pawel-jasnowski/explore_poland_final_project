from decimal import Decimal

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db.models import Model, CharField, TextField, DecimalField, FileField, ForeignKey, DateField, CASCADE, ImageField
from multiselectfield import MultiSelectField

REGION = {
    ("Sea", "Sea"),
    ("Mountains", "Mountains"),
    ("Lakes", "Lakes")
}

OBJECT = {
    ("Hotel", "Hotel"),
    ("Apartment", "Apartment"),
    ("Cottage", "Cottage")
}

FACILITIES_CHOICES = ((1, 'Swimming pool'), (2, 'Free parking outside'), (3, 'Wi-Fi'), (4, 'Pet friendly'), (5, 'SPA'),
                      (6, 'Private kitchen'), (7, 'Bike rating'), (8, 'BBQ Place'), (9, 'coffee maker'),
                      (10, 'family room'))

class Places(Model):
    place_name = CharField(max_length=120, blank=False, unique=True)
    city = CharField(max_length=50, null=False)
    region = CharField(max_length=20, choices=REGION, null=False, blank=False)
    object_type = CharField(max_length=20, choices=OBJECT)
    price_per_night = DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('50.00'))])
    facilities = MultiSelectField(choices=FACILITIES_CHOICES, max_choices=10, max_length=100, blank=False, null=False,
                                  default='')
    description = TextField(null=False)
    image = FileField(null=False, blank=False, default="")

    def __str__(self):
        return f"{self.place_name} ({self.region},{self.city})"


class PlacesImage(Model):
    places = ForeignKey(Places, default=None, on_delete=CASCADE)
    images = FileField(upload_to="places_img")


class Booking(Model):
    user = ForeignKey(User, related_name="user_bookings", on_delete=CASCADE)
    start_date = DateField()
    end_date = DateField()
    total_price = DecimalField(max_digits=10, decimal_places=2)
    place = ForeignKey(Places, related_name='bookings', on_delete=CASCADE)

    def __str__(self):
        return f"Duration {self.end_date - self.start_date}"

    def calculate_price(self):
        return self.place.price_per_night * self.get_total_days()

    def get_total_days(self):
        return (self.end_date - self.start_date).days
