from django.shortcuts import render


def test_response(request):
    return render(request, 'home.html')
