from django.forms import ModelForm, ClearableFileInput

from .models import Places


class PlacesForm(ModelForm):
    class Meta:
        model = Places
        fields = '__all__'
        widgets = {
            'images': ClearableFileInput(attrs={'multiple': True}),
        }

