from django.db import models

# Create your models here.

GENDERS = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('U', 'Unknown'),
]


class Pet(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField(blank=True)
    species = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDERS)