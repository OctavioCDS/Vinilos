from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from sweetify import info, success, warning, error

def principal(request):
    return render(request,'principal.html')
