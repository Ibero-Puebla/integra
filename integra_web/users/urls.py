from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.users, name='users'),
    # ex: /polls/5/results/
    path('<int:question_id>/devices/', views.devices, name='devices'),
    # ex: /polls/5/vote/
    path('<int:question_id>/humidity/', views.humidity, name='humidity'),
    path('<int:question_id>/temperature/', views.temperature, name='temperature'),
    path('<int:question_id>/uvauvb/', views.uvauvb, name='uvauvb'),
    path('<int:question_id>/air/', views.air, name='air'),
]
