from rest_framework import serializers

from .models import api_author, api_book
# It's necessary to serialize User also
from django.contrib.auth.models import User

class user_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']

class api_author_name_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = api_author
        fields = ['id','name']


class api_author_serializer(serializers.HyperlinkedModelSerializer):
    added_by_id = user_serializer()

    class Meta:
        model = api_author
        # fields = ('id','name', 'created_date', 'added_by_id')
        fields = '__all__'

class api_book_serializer(serializers.HyperlinkedModelSerializer):
    # added_by_id = user_serializer()
    # author_id = api_author_name_serializer()

    class Meta:
        model = api_book
        # fields = ('id','title', 'description', 'created_date', 'added_by_id', 'author_id')
        fields = '__all__'
        depth = 1


