from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Adventurer
from .forms import JourneyForm, AdventurerForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def adventurers_index(request):
    if request.method == 'POST':
        adventurer_form = AdventurerForm(request.POST)
        if adventurer_form.is_valid():
            adventurer_form.save()
            return redirect('index')
    adventurers = Adventurer.objects.all()
    adventurer_form = AdventurerForm()
    context = {'adventurers': adventurers, 'adventurer_form': adventurer_form}
    return render(request, 'adventurers/index.html', context)

def adventurers_detail(request, name):
    adventurer = Adventurer.objects.get(name=name)
    journey_form = JourneyForm()
    return render(request, 'adventurers/detail.html', { 'adventurer': adventurer, 'journey_form': journey_form})

def add_journey(request, adventurer_id, name):
    form = JourneyForm(request.POST)
    if form.is_valid():
        new_journey = form.save(commit=False)
        new_journey.adventurer_id = adventurer_id
        new_journey.save()
    return redirect('detail', name=name)