from django.db import models

# Create your models here.
class Adventurer(models.Model):
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    weapon = models.CharField(max_length=100)
    health = models.IntegerField()
    wealth = models.IntegerField()

    def __str__(self):
        return self.name