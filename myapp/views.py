from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = ContactForm()
    return render(request, 'myapp/form1.html', {'form': form})