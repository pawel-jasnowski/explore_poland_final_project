from django.urls import path, include, reverse_lazy
from django.views.generic import ListView
from .import views

urlpatterns = [
    path('create_review/', views.create_new_review, name='create_review'),
    # path('create', views.create_new_review, name='create_review'),
    # path('view', views.ReviewList, name='view_review'),

    ]