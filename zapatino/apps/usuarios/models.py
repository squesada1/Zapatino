from django.db import models


class datos_usuarios(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(null = True)
    
def __unicode__(self):
    return "%s - %s" %(self.nombre)