from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import CreateReview
from review_app.models import Review
# from .forms import ReviewYourReservation, CreateReview
# Create your views here.

# def create_new_review(request):
#     return render(request, 'home.html')

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
        return redirect('login_user')

#
# def ReviewList(LoginRequiredMixin, ListView):
#     template_name = 'review_form_karola.html'



