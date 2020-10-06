from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Adventurer, Enemy
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
    future_enemies = Enemy.objects.exclude(id__in = adventurer.enemys.all().values_list('id'))
    journey_form = JourneyForm()
    return render(request, 'adventurers/detail.html', { 
        'adventurer': adventurer, 
        'journey_form': journey_form,
        'enemys': future_enemies
    })

def add_journey(request, adventurer_id, name):
    form = JourneyForm(request.POST)
    if form.is_valid():
        new_journey = form.save(commit=False)
        new_journey.adventurer_id = adventurer_id
        new_journey.save()
    return redirect('detail', name=name)

def adventurers_delete(request, adventurer_id):
    Adventurer.objects.get(id=adventurer_id).delete()
    return redirect('index')

def adventurers_edit(request, adventurer_id, name):
    adventurer = Adventurer.objects.get(id=adventurer_id)
    if request.method == 'POST':
        adventurer_form = AdventurerForm(request.POST, instance=adventurer)
        if adventurer_form.is_valid():
            adventurer_form.save()
            return redirect('detail', name=name)
    else:
        adventurer_form = AdventurerForm(instance=adventurer)
    context = {'adventurer': adventurer, 'adventurer_form': adventurer_form}
    return render(request, 'adventurers/edit.html', context)

def assoc_enemy(request, adventurer_id, name, enemy_id):
    Adventurer.objects.get(id=adventurer_id).enemys.add(enemy_id)
    return redirect('detail', name=name)