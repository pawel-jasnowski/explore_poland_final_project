from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

from .forms import CreateReview

from review_app.models import Review
# from .forms import ReviewYourReservation, CreateReview
# Create your views here.


def create_new_review(request):
    if request.user.is_authenticated:
         # Do something for logged-in users.
        if request.method == 'POST':
            form = CreateReview(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home_page_app:main')
        else:
             form = CreateReview()
        return render(request, 'create_review_test.html', {'form': form})
    else:
        # Do something for anonymous users.
        messages.success(request, f'You must be logged it to add some review!')
        return redirect('login_user')

class ReviewView(View):
    def get(self, request):
        return render(
            request, template_name='review_all.html', context={'reviews': Review.objects.all()}
        )
def view_all_reviews(request):
    return render(
        request,
        template_name='review_form.html',
        context={'reviews': Review.objects.all()}
                    )

