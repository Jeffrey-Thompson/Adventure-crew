from django.contrib import admin
from .models import Adventurer, Journey, Enemy, Gear

# Register your models here.
admin.site.register(Adventurer)
admin.site.register(Journey)
admin.site.register(Enemy)
admin.site.register(Gear)
