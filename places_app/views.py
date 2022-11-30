from urllib import request

from django.shortcuts import render, get_object_or_404, redirect
from .forms import PlacesForm, BookingForm
from .models import Places, Booking
from django.http import HttpResponseRedirect

def all_places(request):
    all_offers = Places.objects.all()
    return render(request, 'place.html', {'places': all_offers})


def new_place(request):
    form = PlacesForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

    return render(request, 'place_form.html', {'form': form})


def edit_place(request, id):
    place = get_object_or_404(Places, pk=id)
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


# def get_detail(request, id):
#     place = get_object_or_404(Places, pk=id)
#     if request.method == "POST":
#         place.detail()
#         return redirect(place)
#     return render(request, ".html", {'place': place})


def get_reservation(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BookingForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()

            return redirect(all_places)

    else:
        form = BookingForm()

    return render(request, 'reservation.html', {'form': form})



    """
    form = BookingForm(request.POST or None)

    print(form)

    if form.is_valid():
        form.save()

    return render(request, "reservation.html", {'form': form})"""

# def get_summary(request):
#     booking = get_object_or_404(Booking, pk=id)
#
#     return render(request, "summary.html", {'booking': booking})

def get_summary(request):
    booking = BookingForm(request.POST or None)

    if booking.is_valid():
        booking.save()

    return render(request, "summary.html", {'booking': booking})

# class BookingView(FormView):
#     form_class = BookingForm
#     template_name = 'reservation.html'
#
#     def form_valid(self, form):
#         data = form.cleaned_data
#
#         booking = Booking.object.create(
#             user=request.user,
#             start_date=data['start_date'],
#             end_date=data['end_date']
#
#         )
#         booking.save()
