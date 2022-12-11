from django.urls import path
from home_page_app.views import test_response, test_page


app_name = 'home_page_app'
urlpatterns = [
    path('home/', test_response),
    path('', test_page, name='main'),

]
