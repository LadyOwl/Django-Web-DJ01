from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def data_view(request):
    return render(request, 'data.html')

def test_view(request):
    return render(request, 'test.html')

def page3_view(request):
    return render(request, 'page3.html')

def page4_view(request):
    return render(request, 'page4.html')

# Create your views here.
