from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView

from .models import Places
from .forms import PlacesForm
from .filters import PlacesFilter



# def all_places(request):
#     qs = Places.objects.all()
#     region = request.GET.get('region')
#     context = {
#         'queryset':qs
#     }
#     return render(request, 'place.html', context)

def all_places(request):
    all_offers = Places.objects.all()
    return render(request, 'place.html', {'places': all_offers})

# def filter(request):
#     place = Places.objects.get(pk=id)
#     myFilter = PlacesFilter()
#     context={'place':place, "myFilter":myFilter}
#     return render(request, 'place.html', context)


def new_place(request):
    form = PlacesForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

    return render(request, 'place_form.html', {'form': form})

def edit_place(request, id):
    place = get_object_or_404(Places, pk=id )
    form = PlacesForm(request.POST or None, request.FILES or None, instance=place)

    if form.is_valid():
        form.save()
        return redirect(all_places)

    return render(request, 'place_form.html', {'form': form})

def delete_place(request, id):
    place = get_object_or_404(Places, pk=id)

    if request.method == "POST":
        place.delete()
        return redirect(all_places)

    return render(request, 'confirm_deletion.html', {'place': place})



def get_detail(request, id):
    # place=Places.objects.get(pk=id)
    # return render(request, 'detail.html',{{'place':place}})
    place = get_object_or_404(Places, pk=id)

    if request.method == "POST":
        place.detail()
        return redirect(place)
    return render(request, "detail.html", {'place': place} )




