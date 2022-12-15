from django.forms import ModelForm, Textarea, Select
from django import forms

from .models import Review

RATING_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ]
class CreateReview(ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'review_body')

        widgets = {
            'rating': Select(attrs={'class': 'form-control'}, choices=RATING_CHOICES),
            'review_body': Textarea(attrs={'class': 'form-control'}),
        }




# RATING_CHOICES = [
#     ('1', '1'),
#     ('2', '2'),
#     ('3', '3'),
#     ('4', '4'),
#     ('5', '5'),
#     ('6', '6'),
#     ('7', '7'),
#     ('8', '8'),
#     ('9', '9'),
#     ]
# class CreateReview(ModelForm):
#     pass
# def rating_validator(value):
#     pass
#
# def review_body_validator(value):
#     pass
#
# class ReviewYourReservation(LoginRequiredMixin, ModelForm):
#
#     class Meta:
#         model = Review
#         fields = "__all__"  # all fields from model Review
#         # fields = ('rating', 'review_body')
#
#         # widgets = {
#         #     'rating': forms.Select(attrs={'class':'form-control'}, choices=RATING_CHOICES),
#         #     'review_body': forms.Textarea (attrs={'class':'form-control'}),
#         # }



