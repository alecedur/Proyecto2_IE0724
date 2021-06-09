from django.db import models

# Create your models here.

GENDERS = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('U', 'Unknown'),
]

HOUR = [
    ('1', '8:00',
     '2', '9:00',
     '3', '10:00',
     '4', '11:00',
     '5', '12:00',
     '6', '13:00',
     '7', '14:00',
     '8', '15:00',)
]
class superUser(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class users(models.Model): 
    email = models.EmailField(unique = True)
    name = models.CharField(max_length = 20)
    password = models.CharField(max_length = 30)
    isSuper = models.BooleanField(default = False) 
 
class providers(models.Model):
    providerName = models.CharField(unique=True, max_length=50)
class appointment(models.Model):
    patient = models.ForeignKey(users, default=None, on_delete=models.CASCADE, related_name='patientName')
    provider = models.ForeignKey(providers, default=None, on_delete=models.CASCADE, related_name='doctorProviders')
    appointmentDate = models.DateTimeField(default=None)
    takenDate = models.BooleanField(default=False)
# class Pet(models.Model):
#     name = models.CharField(max_length=20)
#     age = models.PositiveIntegerField(blank=True)
#     species = models.CharField(max_length=20)
#     gender = models.CharField(max_length=1, choices=GENDERS)