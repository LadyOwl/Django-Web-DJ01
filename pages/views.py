from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return HttpResponse("<p1>Главная страница</p1>")
def data_view(request):
    return HttpResponse("<p1>Страница DATA</p1>")
def test_view(request):
    return HttpResponse("<p1>Страница TEST</p1>")

# Create your views here.
