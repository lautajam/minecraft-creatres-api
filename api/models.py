from django.db import models
from .choices import type_creature

# Create your models here.
class Creature(models.Model):
    name = models.CharField(max_length=50)
    type_creature = models.CharField(max_length=20, choices=type_creature)
    health_points = models.PositiveIntegerField()
    # image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    biome = models.CharField(max_length=50) # ¿CHOICE? Make a list with all the biomes / It has to be several things
    drop = models.CharField(max_length=150) # ¿CHOICE? It has to be several things
    special_action = models.TextField()