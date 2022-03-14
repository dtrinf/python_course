from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class player(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True)
    steam_user = models.CharField(max_length = 100)
    twitter_user = models.CharField(max_length = 100)
    discord_user = models.CharField(max_length = 100)

    def __str__(self):
        return self.user.username



