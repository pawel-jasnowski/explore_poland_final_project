from django.db.models import Model, TextField, IntegerField, ForeignKey, CASCADE

from django.contrib.auth.models import User
from places_app.models import Places
# Create your models here.
class Review(Model):
    rating = IntegerField()
    review_body = TextField(max_length=500)
    author = ForeignKey(User, on_delete=CASCADE, default='')
    place_name = ForeignKey(Places, on_delete=CASCADE, default='')