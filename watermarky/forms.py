
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django .forms import ModelForm
from watermarky.models import Imaj

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2' )

# class ImajForm(ModelForm):
#     class Meta:
#         model = Imaj
#         fields = ('pseudo', 'photo')