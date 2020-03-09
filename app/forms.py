from django.contrib.auth.forms import UserCreationForm

from app.models import Person


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Person
        fields = ('username',)
