from django.forms import ModelForm
from .models import User


class SaveName(ModelForm):
    class Meta:
        model = User
        fields = ('name',)
