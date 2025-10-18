from django.shortcuts import render
from django.http import HttpResponse

def data_view(request):
    return HttpResponse("Страница DATA")
def test_view(request):
    return HttpResponse("Страница TEST")

# Create your views here.
