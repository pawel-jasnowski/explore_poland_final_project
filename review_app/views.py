from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, FormView
from django.urls import reverse_lazy

from review_app.models import Review
from review_app.forms import ReviewYourReservation
# Create your views here.

def review(request):
    return HttpResponse('Review .. ')

class CreateReviewForm(CreateView):
    template_name = 'form.html'
    form_class = ReviewYourReservation
    success_url = reverse_lazy('review/create')
