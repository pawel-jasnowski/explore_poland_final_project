from django.db.models import Model, TextField, CharField, IntegerField, \
    ForeignKey, CASCADE
from django import forms
from django.contrib.auth.models import User
from places_app.models import Places

# Create your models here.
class Review(Model):
    # name = TextField(max_length = 30)
    rating = IntegerField()
    review_body = TextField(max_length=500)
    author = ForeignKey(User, on_delete=CASCADE) # CASCADE will delete all the post from deleted user
    place_name = ForeignKey(Places, on_delete=CASCADE, default ='')

