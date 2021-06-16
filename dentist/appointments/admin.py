from django.contrib import admin
from .models import superUser, users, providers, appointment

# Register your models here.
admin.site.register(users)
admin.site.register(superUser)
admin.site.register(providers)
admin.site.register(appointment)