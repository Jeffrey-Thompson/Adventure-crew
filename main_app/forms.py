from django.forms import ModelForm
from .models import Journey, Adventurer

class AdventurerForm(ModelForm):
    class Meta:
        model = Adventurer
        fields = ['name', 'style', 'weapon', 'health', 'wealth']

class JourneyForm(ModelForm):
    class Meta:
        model = Journey
        fields = ['goal', 'challenge', 'reward']