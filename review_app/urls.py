from django.urls import path

from .import views


urlpatterns = [
    path('create_review/<int:place_id>/', views.create_new_review, name='create_review'),
    path('view_all_reviews/<int:place_id>/', views.view_all_reviews, name='view_review'),
   ]