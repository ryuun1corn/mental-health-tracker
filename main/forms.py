from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from main.models import MoodEntry


class MoodEntryForm(ModelForm):
    class Meta:
        model = MoodEntry
        fields = ["mood", "feelings", "mood_intensity"]


class RegisterForm(UserCreationForm):
    """Form to Create new User"""

    usable_password = None

    class Meta:
        model = get_user_model()
        fields = ["username", "password1", "password2"]

