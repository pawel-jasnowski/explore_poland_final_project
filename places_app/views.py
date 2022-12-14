from django.shortcuts import render

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
        place = Places.objects.get(id=id)

        if 'action' in request.session.keys() and request.session['action'] == 'confirm':

            confirmed = request.POST.get('confirmed')

            if confirmed == 'cancel':
                del request.session['action']
                del request.session['start_date']
                del request.session['end_date']
                del request.session['total_price']

                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            Booking.objects.create(
                place=place,
                user=request.user,
                start_date=request.session['start_date'],
                end_date=request.session['end_date'],
                total_price=request.session['total_price']
            )

            messages.success(request, 'Your booking has been saved')

            del request.session['action']
            del request.session['start_date']
            del request.session['end_date']
            del request.session['total_price']

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        if start_date == '' or end_date == '':
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

        request.session['action'] = 'confirm'
        request.session['start_date'] = start_date
        request.session['end_date'] = end_date
        request.session['total_price'] = str(total_price)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    all_place = Places.objects.get(id=id)
    images = all_place.placesimage_set.all()

    return render(request, 'reservation.html', {
        'all_place': all_place,
        'images': images,
    })

def get_summary(request, id):
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    place = Places.objects.get(id=id)

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

    context = {'start_date': start_date, 'end_date': end_date, 'place': place, 'total_price': total_price}

    return render(request, "reservation.html", context)


# def new_place(request):
#     form = PlacesForm(request.POST or None, request.FILES or None)
#
#     if form.is_valid():
#         form.save()
#
#     return render(request, 'place_form.html', {'form': form})
#
#
# def edit_place(request, id):
#     place = get_object_or_404(Places, pk=id)
#     form = PlacesForm(request.POST or None, request.FILES or None, instance=place)
#
#     if form.is_valid():
#         form.save()
#         return redirect(all_places)
#
#     return render(request, 'place_form.html', {'form': form})
#
#
# def delete_place(request, id):
#     place = get_object_or_404(Places, pk=id)
#
#     if request.method == "POST":
#         place.delete()
#         return redirect(all_places)
#
#     return render(request, 'confirm_deletion.html', {'place': place})


