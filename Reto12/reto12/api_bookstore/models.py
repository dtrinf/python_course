from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Book model
class api_book(models.Model):
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    created_date = models.DateField(auto_now_add=True)
    author_id = models.ForeignKey('api_author', on_delete=models.CASCADE)
    added_by_id = models.ForeignKey(User, on_delete=models.CASCADE)

# Author model
class api_author(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateField(auto_now_add=True)
    added_by_id = models.ForeignKey(User, on_delete=models.CASCADE)


