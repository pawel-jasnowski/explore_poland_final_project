from django.urls import path
from home_page_app.views import test_response, test_page
from django.views.generic import TemplateView

app_name = 'home_page_app'
urlpatterns = [
    path('home/', test_response),
    path('', test_page)
]