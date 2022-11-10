from django.forms import ModelForm, CharField, IntegerField
from django.core.exceptions import ValidationError

from .models import Review

def rating_validator(value):
    if value < 0 and value > 10:
        raise ValidationError('Rating must be between 0-9')

class ReviewYourReservation(ModelForm):

    class Meta:
        model = Review
        fields ='__all__'

    rating = IntegerField (validators=[rating_validator])          # walidacja ? / np. punktacja 0-10
    review_body = CharField(max_length=500)     # jakieś validacje dotyczące tego pola ?! np= zakaz przekleństw

