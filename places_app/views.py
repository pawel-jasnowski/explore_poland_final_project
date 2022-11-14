from django.shortcuts import render
from .models import Places



def all_places(request):
    all_offers = Places.objects.all()
    return render(request, 'place.html', {'places': all_offers})

