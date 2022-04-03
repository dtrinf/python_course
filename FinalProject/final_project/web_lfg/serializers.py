# serializers.py in the users Django app
from django.db import transaction
from rest_framework import serializers

from web_lfg.models import player



class player_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = player
        ## All fields can be defined in an easy way
        fields = '__all__'