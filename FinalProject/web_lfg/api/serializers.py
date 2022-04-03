# serializers.py in the users Django app
from django.db import transaction
from rest_framework import serializers

from api.models import CustomUser


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        ## All fields can be defined in an easy way
        fields = ['id','username','twitter_user']


    # def get_extra_data(self, instance):
    #     if instance.is_superuser is not True:
    #         extra_data = instance.socialaccount_set.all()[0].extra_data
    #         return extra_data
