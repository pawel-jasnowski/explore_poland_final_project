from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, FormView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import CreateReview
from review_app.models import Review
# from .forms import ReviewYourReservation, CreateReview
# Create your views here.


def create_new_review(request):
    render(request, 'review_form.html', {})

def review_list(LoginRequiredMixin, ListView):
    template_name = 'review_all.html'
    model = Review

    
