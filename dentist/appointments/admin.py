from django.contrib import admin
from .models import superUser, users

# Register your models here.
admin.site.register(users)
admin.site.register(superUser)