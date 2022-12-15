from django.forms import ModelForm, ValidationError, DateField
from datetime import date
from django.forms.widgets import DateInput
from .models import Places, Booking
from django import forms

# class PlacesForm(ModelForm):
#     class Meta:
#         model = Places
#         fields = '__all__'
#
#
# class PastMonthField(DateField):
#     def validate(self, value):
#         super().validate(value)
#         if value >= date.today():
#             raise ValidationError('Only past dates allowed here.')
#
#
# class BookingForm(ModelForm):
#     start_date = forms.DateField(
#         required=True,
#         widget=forms.widgets.DateInput(
#             attrs={
#                 "placeholder": "Start date",
#                 'type': 'date'
#             }
#         ),
#     )
#
#     end_date = forms.DateField(
#         required=True,
#         widget=forms.widgets.DateInput(
#             attrs={
#                 "placeholder": "Start date",
#                 'type': 'date'
#             }
#         ),
#     )
#     class Meta:
#         model = Booking
#         fields = '__all__'
#
#
