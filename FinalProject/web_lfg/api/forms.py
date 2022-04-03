
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# Custom creation form userd to create a new user
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model() # Get current user model used in the project
        fields = ('email', 'username',)


# Custom change form used to update a user
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model() # Get current user model used in the project
        fields = ('email', 'username',)