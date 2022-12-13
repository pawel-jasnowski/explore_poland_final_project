from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import View

from .forms import CreateReview
from review_app.models import Review
from places_app.models import Places


# Create your views here.

def create_new_review(request, place_id):
    if request.user.is_authenticated:
        our_user = request.user
        our_place = get_object_or_404(Places, pk=place_id) # instance of PLACE
         # Do something for logged-in users.
        if request.method == 'POST':
            form = CreateReview(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                data = Review()
                data.rating = form.cleaned_data['rating']
                data.review_body = form.cleaned_data['review_body']
                data.author = our_user
                data.place_name = our_place
                data.save()
                return redirect('home_page_app:main')
        else:
            form = CreateReview()
        return render(request, 'create_review_test.html', {'form': form})
    else:
        return redirect('login_user')

def view_all_reviews(request, place_id):
    our_place = get_object_or_404(Places, pk=place_id)
    return render(
        request,
        template_name='review_form_karola.html',
        context={'reviews': Review.objects.filter(place_name=our_place).all()}

            )
