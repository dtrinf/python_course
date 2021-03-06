from django.db import models
from django.contrib.auth.models import AbstractUser

#Libraries for CustomUserManager
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

class CustomUser(AbstractUser):
    twitter_user = models.CharField(max_length=50, unique=True, null=True)
    

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager.
    """
    def create_user(self, username, email, password, twitter_user, **extra_fields):
        """
        Create and save a User with the given username and password.
        """
        # if not email:
        #     raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.twittwer_user = twitter_user
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, twitter_user, **extra_fields):
        """
        Create and save a SuperUser with the given username and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        if extra_fields.get('is_active') is not True:
            raise ValueError(_('Superuser must have is_active=True.'))

        return self.create_user(username, email, twitter_user, password, **extra_fields)