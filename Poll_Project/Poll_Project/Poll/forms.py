from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Poll

class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'option_one', 'option_two', 'option_three','option_four']


class RegisterUser(UserCreationForm):
    class Meta:
        model=User
        fields=('first_name','last_name','username','email','password1','password2')
