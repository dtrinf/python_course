from django.shortcuts import render

from rest_framework import viewsets

# Serializers imported to be used with the view
from .serializers import player_serializer
# Objects models imported to be serialized
from .models import player

# Create your views here.

class player_viewset(viewsets.ModelViewSet):
    queryset = player.objects.all()
    serializer_class = player_serializer
