from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    return render (request, "login.html")

def novo_usuario(request):
    return render(request, "novo-usuario.html")

def logout(request):
    auth_logout(request)
    return redirect('login')