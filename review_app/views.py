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

class LockedView(LoginRequiredMixin):
    login_url = "admin:login"

class CreateReviewForm(LockedView, CreateView):
    template_name = 'form.html'
    form_class = ReviewYourReservation
    success_url = reverse_lazy('review_all')
    
class SignUpView(CreateView):
    template_name = 'sign_up_template.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    
