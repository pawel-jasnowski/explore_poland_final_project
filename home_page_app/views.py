from django.shortcuts import render


def test_response(request):
    return render(request, 'home_page/home.html' )
