from django.db import models
from .choices import type_creatures

# Create your models here.
class Creatures(models.Model):
    name = models.CharField(max_length=50)
    type_creatures = models.CharField(max_length=2, choices=type_creatures)
    health_points = models.PositiveIntegerField()
    # image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    biome = models.CharField(max_length=50) # ¿CHOICE? Make a list with all the biomes / It has to be several things
    drop = models.CharField(max_length=150) # ¿CHOICE? It has to be several things
    special_action = models.TextField()