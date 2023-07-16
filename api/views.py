from rest_framework import viewsets
from .serializers import CreatureSerializer
from .models import Creature

# Create your views here.
class CreatureViewSet(viewsets.ModelViewSet):
    queryset = Creature.objects.all()
    serializer_class = CreatureSerializer