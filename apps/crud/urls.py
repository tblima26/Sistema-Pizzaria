from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nova-pizza/', views.nova_pizza, name='nova_pizza'),
    path('nova-pizza-sucesso/', views.nova_pizza_sucesso, name='nova_pizza_sucesso'),
    path('pizza/<int:pizza_id>/excluir/',views.excluir_pizza,
    name='excluir_pizza'),
    path('pizza/<int:pizza_id>/alterar/',views.alterar_pizza,
    name='alterar_pizza'),

]