from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('data/', views.data_view),
    path('test/', views.test_view),
]