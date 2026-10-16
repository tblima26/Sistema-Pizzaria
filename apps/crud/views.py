from django.shortcuts import render, redirect
from .models import Pizza

# Create your views here.
def index(request):
  return render(request, "index.html")

def nova_pizza(request):
  return render(request, 'nova-pizza.html',{
    'categorias': Pizza.CATEGORIAS
  })