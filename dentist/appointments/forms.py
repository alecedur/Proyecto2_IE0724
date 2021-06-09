from django import forms
from .models import superUser, users


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
