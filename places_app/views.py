from django.shortcuts import render, get_object_or_404, redirect
from .models import Places
from .forms import PlacesForm



def all_places(request):
    all_offers = Places.objects.all()
    # filter_offers = PlacesFilter(request.GET, queryset=all_offers)
    # return render(request, 'place.html', {'filter': filter_offers})
    return render(request, 'filter.html', {'places': all_offers})

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
    place = get_object_or_404(Places, pk=id)
    images=PlacesImage.objects.filter(places=place.id)
    for image in images:
        print(image.images.url)
    if request.method == "POST":
        place.detail()
        return redirect(place)
    return render(request, "detail.html", {'place': place, 'images': images} )


def place_filter(request):
    all_offers = Places.objects.all()
    filter_offers = PlacesFilter(request.GET, queryset=all_offers)
    return render(request, 'filter.html', {'filter': filter_offers})

class MountainView(ListView):
    template_name="place.html"
    def get_queryset(self):
        return Places.objects.filter(region__exact='Mountains').all()

class LakesView(ListView):
    template_name="place.html"
    def get_queryset(self):
        return Places.objects.filter(region__exact='Lakes').all()

class SeaView(ListView):
    template_name="place.html"
    def get_queryset(self):
        return Places.objects.filter(region__exact='Sea').all()