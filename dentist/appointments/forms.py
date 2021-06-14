from django import forms
from .models import superUser, users
from datetime import datetime

class loginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    superUser = forms.BooleanField(required=False)

class usersForm(forms.ModelForm):
    class Meta:
        model = users
        fields = [
            'email',
            'name',
            'password',
        ]
        labels = {
            'email' : 'email',
            'name' : 'Name',
            'password' : 'Password',
        }
    key = forms.CharField(required=False, max_length=20)


class newAppointment(forms.Form):
    date = forms.DateField(required=True)
    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return date

class superuserForm(forms.ModelForm):
    class Meta:
        model = superUser
        fields = [
            'email',
            'name',
            'password',
        ]
        labels = {
            'email' : 'email',
            'name' : 'Name',
            'password' : 'Password',            
        }
    key = forms.CharField(required=True, max_length=20)    
# class PetForm(forms.ModelForm):

#     class Meta:
#         model = Pet
#         fields = [
#             'name',
#             'gender',
#             'age',
#             'species',
#         ]
#         labels = {
#             'name': 'Name',
#             'gender': 'Gender',
#             'age': 'Age',
#             'species': 'Species',
#         }
