from django.shortcuts import render

from rest_framework import viewsets

# Serializers imported to be used with the view
from .serializers import CustomUserSerializer
# Objects models imported to be serialized
from .models import CustomUser

# Create your views here.

class CustomUser_viewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer