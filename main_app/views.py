from django.shortcuts import render
from django.http import HttpResponse
from .models import Adventurer

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def adventurers_index(request):
    adventurers = Adventurer.objects.all()
    return render(request, 'adventurers/index.html', {'adventurers': adventurers})

def adventurers_detail(request, name):
    adventurer = Adventurer.objects.get(name=name)
    return render(request, 'adventurers/detail.html', { 'adventurer': adventurer})