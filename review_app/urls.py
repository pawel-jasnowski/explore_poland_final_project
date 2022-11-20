from django.urls import path, include, reverse_lazy
from .import views

urlpatterns = [
    path('create', views.create_new_review, name='create_review'),
    path('view', views.review_list, name='view_review'),

    ]