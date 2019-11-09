from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='Primeiro Nome', max_length=30, required=True, help_text='Optional.')
    last_name = forms.CharField(label='Ultimo Nome', max_length=30, required=True, help_text='Optional.')
    email = forms.EmailField(label='E-mail', max_length=254, help_text='Informe um email válido.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
