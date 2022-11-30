from django.shortcuts import render


def test_response(request):
    return render(request, 'home.html')

def test_page(request):
    return render(request, 'home_page.html')



