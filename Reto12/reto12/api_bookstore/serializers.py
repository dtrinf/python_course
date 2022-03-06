from rest_framework import serializers

## New models imported to define its serialization
from .models import api_author, api_book
## It's necessary to serialize User also
from django.contrib.auth.models import User

## Intermediate serializer in case we want to define the fields will show the reference to User object
class user_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']

## Intermediate serializer in case we want to define the fields will show the reference to Author object
class api_author_name_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = api_author
        fields = ['id','name']


## Serializer to be used with rest_framework
class api_author_serializer(serializers.HyperlinkedModelSerializer):
    ## We oberride the field "added_by_id", it will show only the fields defined into the intermediate serializer
    added_by_id = user_serializer()

    class Meta:
        model = api_author
        ## All fields can be defined in an easy way
        fields = '__all__'

class api_book_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = api_book
        # fields = ('id','title', 'description', 'created_date', 'added_by_id', 'author_id')
        fields = '__all__'
        depth = 1 # All fields with a relation will be printed with the defined depth


