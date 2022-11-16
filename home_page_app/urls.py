from django.urls import path
from home_page_app.views import test_response, test_page
from django.views.generic import TemplateView


urlpatterns = [
    path('home/', test_response),
    path('home_page/', test_page, name='main')
]