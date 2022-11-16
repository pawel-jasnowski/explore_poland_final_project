from django.forms import ModelForm, CharField, IntegerField, Textarea
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Review

class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'email']

        def save(self, commit=True):
            self.instance.is_active=False
            return super().save(commit)

def rating_validator(value):
    pass

def review_body_validator(value):
    pass

class ReviewYourReservation(LoginRequiredMixin, ModelForm):

    class Meta:
        model = Review
        fields ='__all__'

    rating = IntegerField (min_value=0, max_value=9)          # walidacja ? / np. punktacja 0-10
    review_body = CharField(max_length=500, widget=Textarea)     # jakieś validacje dotyczące tego pola ?! np= zakaz przekleństw
   
