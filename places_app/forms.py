from django.forms import ModelForm
from .models import Places

class PlacesForm(ModelForm):
    class Meta:
        model = Places
        fields = '__all__'