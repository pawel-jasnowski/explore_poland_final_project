from django.forms import ModelForm, CharField, IntegerField, Textarea
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Review


class CreateReview(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"  # all fields from model Review



