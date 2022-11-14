from django.forms import ModelForm, CharField, IntegerField, Textarea
from django.core.exceptions import ValidationError

from .models import Review

from datetime import date

def rating_validator(value):
    pass

def review_body_validator(value):
    pass

class ReviewYourReservation(ModelForm):

    class Meta:
        model = Review
        fields ='__all__'

    name = CharField(max_length=30, widget=Textarea)
    rating = IntegerField (min_value=0, max_value=9)          # walidacja ? / np. punktacja 0-10
    review_body = CharField(max_length=500, widget=Textarea)     # jakieś validacje dotyczące tego pola ?! np= zakaz przekleństw
    # date = DateFiled()
