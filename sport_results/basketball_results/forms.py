from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BasketballMatch

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Reikalinga. Įveskite galiojantį el. paštą.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class BasketballMatchForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = BasketballMatch
        fields = ['match', 'date', 'team1', 'team2', 'score1', 'score2',]
        labels = {
            'match' : 'Krepšinio lygos pavadinimas',
            'date' : 'Data',
            'team1' : 'Komanda 1',
            'team2' : 'Komanda 2',
            'score1' : 'Taškai komanda 1',
            'score2' : 'Taškai komanda 2',
        }
