from django.forms import ModelForm
from chore_main.models import Chore, Person
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ("role", )

class UserCreationForm(UserCreationForm): #extending built-in form
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user




this is a test


class ChoreModelForm(forms.ModelForm):
    class Meta:
        model = Chore
        fields = (
            "title",
            "master",
            "slave",
            "task",
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['master'].queryset = Person.objects.filter(role="Master")
        self.fields['slave'].queryset = Person.objects.filter(role="Slave")