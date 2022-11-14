"""explore_poland URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.conf import settings
from django.conf.urls.static import static

from review_app import views
from review_app.models import Review
from review_app.forms import ReviewYourReservation


urlpatterns = [
    path('admin/', admin.site.urls),
    path('review/create', CreateView.as_view(template_name='form.html', form_class=ReviewYourReservation,
                                             success_url=reverse_lazy('review_all')), name='create_review'),
    path('review/update/<pk>', UpdateView.as_view(template_name='form.html', model=Review, form_class=ReviewYourReservation, success_url=reverse_lazy('review_all')), name='update_review'),
    path('review/delete/<pk>', DeleteView.as_view(template_name='delete.html', model=Review, success_url=reverse_lazy('review_all'))),
    path('review/all', ListView.as_view(template_name='review_all.html', model=Review), name='review_all'),
    path('explore/', include('home_page_app.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    


