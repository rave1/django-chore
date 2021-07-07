from django.forms import ModelForm
from chore_main.models import Person
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ("role", )



class ChoreForm(forms.Form):
    title = forms.CharField()
    task = forms.CharField()
    