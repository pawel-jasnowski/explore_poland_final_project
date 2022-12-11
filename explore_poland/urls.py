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
from django.contrib.auth.views import LoginView, LogoutView

from user_app.views import PasswordsChangeView
from home_page_app.views import test_response

# from review_app import views
# from review_app.models import Review
# from review_app.forms import ReviewYourReservation
# from review_app.views import SignUpView, ReviewListView, CreateReviewFormView, feedback_form, sign_up, logout_user


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', include('places_app.urls')),
    path('', include('home_page_app.urls')),
    path('user/', include('user_app.urls')),
    path('user/', include('django.contrib.auth.urls')), #  build in function for user
    path('review/', include('review_app.urls')),
    path('password/', PasswordsChangeView.as_view(template_name='authenticate/change_password.html'), name='password_change'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
