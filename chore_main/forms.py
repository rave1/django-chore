from django.forms import ModelForm
from chore_main.models import Person
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



class ChoreForm(forms.Form):
    title = forms.CharField()
    task = forms.CharField()
    