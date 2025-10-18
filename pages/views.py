from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return HttpResponse('''
        <h1>Главная страница</h1>
        <a href="/data/"><button>Перейти на Data</button></a>
        <a href="/test/"><button>Перейти на Test</button></a>
    ''')
def data_view(request):
    return HttpResponse("<p1>Страница DATA</p1>")
def test_view(request):
    return HttpResponse("<p1>Страница TEST</p1>")

# Create your views here.
