from django.db.models import Model, IntegerChoices, TextField, CharField, IntegerField, OneToOneField
from places_app.models import Places
from django import forms

# Create your models here.
class Review(Model):
    # name = TextField(max_length = 30)
    place = OneToOneField
    rating = IntegerField()
    review_body = TextField(max_length=500)
    # 
    # widgets = {
    #     rating: forms.ChoiceField(attrs={'class': 'form-control'}),
    #     review_body: forms.Textarea(attrs={'class': 'form-control'}),
    # }
