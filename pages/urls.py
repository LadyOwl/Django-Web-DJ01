from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),      # ← добавь эту строку: главная страница = data
    path('data/', views.data_view),
    path('test/', views.test_view),
]