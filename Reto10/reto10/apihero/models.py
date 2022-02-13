from unicodedata import name
from django.db import models

# Create your models here.
class Hero(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name} {self.alias}"

