from django.forms.widgets import PasswordInput, TextInput
from django.forms import ModelForm
from django.contrib.auth.models import User


class LoginForm(ModelForm):
    """ Formulario de login """
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
                'username' : TextInput(
                    attrs={
                        'type' : 'text',
                    }),
                'password' : PasswordInput(
                    attrs={
                        'type' : 'password',
                    }),
        }

