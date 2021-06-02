from django import forms
from .models import Pet


class PetForm(forms.ModelForm):

    class Meta:
        model = Pet
        fields = [
            'name',
            'gender',
            'age',
            'species',
        ]
        labels = {
            'name': 'Name',
            'gender': 'Gender',
            'age': 'Age',
            'species': 'Species',
        }
