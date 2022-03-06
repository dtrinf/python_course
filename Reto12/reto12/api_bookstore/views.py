from django.shortcuts import render

from rest_framework import viewsets

# Serializers imported to be used with the view
from .serializers import api_author_serializer, api_book_serializer, user_serializer
# Objects models imported to be serialized
from .models import api_author, api_book
# User model imported, corresponds to Django registered users
from django.contrib.auth.models import User

from rest_framework import generics



# Create your views here.

class api_author_viewset(viewsets.ModelViewSet):
    queryset = api_author.objects.all().order_by('name')
    serializer_class = api_author_serializer

class api_book_viewset(viewsets.ModelViewSet):
    queryset = api_book.objects.all().order_by('title')
    serializer_class = api_book_serializer

class user_viewset(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = user_serializer

