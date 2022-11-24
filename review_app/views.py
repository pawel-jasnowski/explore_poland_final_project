from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, FormView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from review_app.models import Review
from review_app.forms import ReviewYourReservation
from .forms import SignUpForm
# Create your views here.

def review(request):
    return HttpResponse('Review .. ')

class CreateReviewFormView(LoginRequiredMixin, CreateView):
    template_name = 'form2_karola.html'
    form_class = ReviewYourReservation
    success_url = reverse_lazy('review_all')

class ReviewListView(LoginRequiredMixin, ListView):
    template_name = 'review_all.html'
    model = Review

    
