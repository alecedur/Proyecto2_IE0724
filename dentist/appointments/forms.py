from django import forms
from .models import appointment, superUser, users
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


class newAppointment(forms.ModelForm):
    class Meta:
        model = appointment
        fields = [
            'patient',
            'provider',
            'appointmentDate',
        ]
        labels = {
            'patient' : 'patient',
            'provider' : 'provider',
            'appointmentDate' : 'appointmentDate',
        }


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

