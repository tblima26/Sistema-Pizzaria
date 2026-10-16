from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nova-pizza/', views.nova_pizza, name='nova_pizza')
]