from django.shortcuts import render, get_object_or_404, redirect
from .forms import PlacesForm, BookingForm
from .models import Places, Booking, FACILITIES_CHOICES
from django.contrib import messages
from django.db.models import Q
import datetime
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from datetime import datetime

def check_booking(start_date, end_date, id):
    qs = Booking.objects.filter(
        start_date__lte=start_date,
        end_date__gte=end_date,
        place__id=id
    )

    if len(qs) >= 1:
        return False

    return True

def all_places(request):
    all_offers = Places.objects.all()

    sort_by = request.GET.get('sort_by_price')
    search = request.GET.get('search')
    facilities = request.GET.getlist('facilities')

    if sort_by == 'ASC':
        all_offers = all_offers.order_by('price_per_night')
    else:
        sort_by = 'DESC'
        all_offers = all_offers.order_by('-price_per_night')

    if search is not None and search != "":
        all_offers = all_offers.filter(
            Q(place_name__icontains=search) |
            Q(city__icontains=search) |
            Q(region__icontains=search) |
            Q(object_type__icontains=search))

    if facilities:
        all_offers = all_offers.filter(
            Q(facilities__contains=','.join(facilities))
        )

        facilities = [int(x) for x in facilities]

    context = {
        'all_offers': all_offers,
        'selected_facilities': facilities,
        'search': search,
        'sort_by_price': sort_by,
        'all_facilities': FACILITIES_CHOICES
    }

    return render(request, 'place.html', context)


def place_reservation(request, id):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        place = Places.objects.get(id=id)

        if start_date is '' or end_date is '':
            messages.warning(request, 'Dates cant be empty')

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        if start_date > end_date:
            messages.warning(request, 'Start date cant be > end date')

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        try:
            if not check_booking(start_date, end_date, id):
                messages.warning(request, 'Reservation is already booked in these dates')

                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        except ValidationError as VE:
            messages.error(request, VE.message)

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        datetime_start_date = datetime.strptime(start_date, '%Y-%M-%d')
        datetime_end_date = datetime.strptime(end_date, '%Y-%M-%d')

        total_price = place.price_per_night * (datetime_end_date.day - datetime_start_date.day)

        Booking.objects.create(
            place=place,
            user=request.user,
            start_date=start_date,
            end_date=end_date,
            total_price=total_price
        )

        messages.success(request, 'Your booking has been saved')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    all_place = Places.objects.get(id=id)
    images = all_place.placesimage_set.all()

    return render(request, 'reservation.html', {
        'all_place': all_place,
        'images': images,
    })


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


# def get_reservation(request, slug=None):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#             return redirect(all_places)
#
#     else:
#         form = BookingForm()
#
#     return render(request, 'reservation.html', {'form': form})

# def get_reservation(request, slug=None):
#     all_places = None
#     if slug is not None:
#         try:
#             all_places = Places.objects.get(slug=slug)
#         except Places.DoesNotExist:
#             raise Http404
#         except Places.MultipleObjectsReturned:
#             all_places = Places.objects.filter(slug=slug).first()
#         except:
#             raise Http404
#
#     context = {"all_places": all_places}
#     return render(request, 'reservation.html', context)


# def hotel_detail(request, id):
#     all_places = Places.objects.get(id=id)
#
#     if request.method == 'POST':
#         checkin = request.POST.get('checkin')
#         checkout = request.POST.get('checkout')
#         place = Places.objects.get(id=id)
#         if not check_booking(checkin, checkout, uid, hotel.room_count):
#             messages.warning(request, 'Hotel is already booked in these dates ')
#             return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#
#         HotelBooking.objects.create(hotel=hotel, user=request.user, start_date=checkin
#                                     , end_date=checkout, booking_type='Pre Paid')
#
#         messages.success(request, 'Your booking has been saved')
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


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
