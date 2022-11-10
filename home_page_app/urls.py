from django.urls import path
from home_page_app.views import test_response


urlpatterns = [
    path('home/', test_response)
]