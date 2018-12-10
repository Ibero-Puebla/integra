from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('users/', views.users, name='users'),
    # ex: /polls/5/results/
    path('devices/', views.devices, name='devices'),
    # ex: /polls/5/vote/
    path('humidity/', views.humidity, name='humidity'),
    path('temperature/', views.temperature, name='temperature'),
    path('uvauvb/', views.uvauvb, name='uvauvb'),
    path('air/', views.air, name='air'),
    path('industry/', views.industry, name='industry'),
]
