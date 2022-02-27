from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def userlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        print(email, password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Your have been logged in successfully!')
        else:messages.error(request, 'Invalid credentials!')
    return render(request, 'users/login.html', {})

def usersignup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = CustomUser.objects.create_user(email=email, password=password)
        user.name = name 
        user.save()
        messages.success(request, 'Your account was created successfully!')
    return render(request, 'users/login.html', {})