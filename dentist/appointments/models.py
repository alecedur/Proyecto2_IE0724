from django.db import models

'''
Represante un usuario con nombre, email y password
Si tiene la condicion isSuper es un usuario administrador
'''
class users(models.Model): 
    email = models.EmailField(unique = True)
    name = models.CharField(max_length = 20)
    password = models.CharField(max_length = 30)
    isSuper = models.BooleanField(default = False)
    def __str__(self):
        return self.name
'''
Representan a los doctores que pueden dar citas y tienen un nombre
'''
class providers(models.Model):
    providerName = models.CharField(unique=True, max_length=50)
    def __str__(self):
        return self.providerName
    
'''
Son las citas, cada cita tiene un paciente y un provedor 
No pueden haber citas para personas que no sean pacientes 
o con provedores que no existan
'''
class appointment(models.Model):
    patient = models.ForeignKey(users, default=None, on_delete=models.CASCADE, related_name='patientName')
    provider = models.ForeignKey(providers, default=None, on_delete=models.CASCADE, related_name='doctorProviders')
    appointmentDate = models.DateTimeField(default=None)