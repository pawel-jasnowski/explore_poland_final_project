from django.shortcuts import render, get_object_or_404, redirect
from .models import Places
from .forms import PlacesForm
from .filters import PlacesFilter


# def all_places(request):
#     all_offers = Places.objects.all()
#     return render(request, 'place.html', {'places': all_offers})

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


def all_places(request):
    all_offers = Places.objects.all()
    #     return render(request, 'place.html', {'places': all_offers})
    context ={'places': all_offers}

    filtered_places = PlacesFilter(
        request.GET,
        queryset=Places.objects.all()
    )

    context['filtered_places'] = filtered_places

    return render(request, 'place.html', context=context)
