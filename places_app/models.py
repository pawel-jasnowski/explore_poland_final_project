from django.db.models import Model, CharField, TextField, ImageField, IntegerField

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


class Places(Model):
    place_name = CharField(max_length=120, blank=False, unique=True)
    city = CharField(max_length=50, null=False)
    region = CharField(max_length=20, choices=REGION, null=False, blank=False)
    object_type = CharField(max_length=20, choices=OBJECT)
    price_per_night = IntegerField( null=False, blank=False)
    facilities = CharField(max_length=100, null=False)
    description = TextField(null=False)
    images = ImageField(upload_to="places_img", null=False, blank=False)


    def __str__(self):
        return f"{self.place_name} ({self.region},{self.city}, {self.images})"



