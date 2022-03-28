from django.db import models
from django.contrib.auth.models import AbstractUser
#Libraries for CustomUserManager
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


# Create your models here.
# https://krakensystems.co/blog/2020/custom-users-using-django-rest-framework
# https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
# https://dontrepeatyourself.org/post/django-custom-user-model-extending-abstractuser/


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email="", twitter_user="", password=None, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        # if not email:
        #     raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.twittwer_user = twitter_user
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email="", twitter_user="", password=None, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, twitter_user, password, **extra_fields)


class player(AbstractUser):
    username = models.CharField(max_length=50, unique=True, null=False)
    email = models.EmailField(_('email address'), unique=True)
    twitter_user = models.CharField(max_length=50, unique=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','twitter_user']

    objects = CustomUserManager()

    spouse_name = models.CharField(blank=True, max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    

    def __str__(self):
        return self.email

