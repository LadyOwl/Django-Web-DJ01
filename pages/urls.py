from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('data/', views.data_view),
    path('test/', views.test_view),
    path('page3/', views.page3_view, name='page3'),
    path('page4/', views.page4_view, name='page4'),
]