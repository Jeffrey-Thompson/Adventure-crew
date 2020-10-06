from django.db import models

# Create your models here.
class Enemy(models.Model):
    name = models.CharField(max_length=100)
    species = model.CharField(max_length=100)
    treasure = model.IntegerField()
    health = model.IntegerField()

    def __str__(self):
        return self.name


class Adventurer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    style = models.CharField('combat style', max_length=100)
    weapon = models.CharField('perferred weapon', max_length=100)
    health = models.IntegerField()
    wealth = models.IntegerField()

    def __str__(self):
        return self.name

class Journey(models.Model):
    goal = models.CharField(max_length=100)
    challenge = models.CharField(max_length=100)
    reward = models.CharField(max_length=100)

    adventurer = models.ForeignKey(Adventurer, on_delete=models.CASCADE)

    def __str__(self):
        return f"A Journey for {self.goal}"