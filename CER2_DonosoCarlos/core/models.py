from django.db import models
from .choices import estado

# Create your models here.

class Residencia(models.Model):
    nroResidencia = models.IntegerField()
    nombre_dueño = models.CharField(max_length=30)

    def __str__(self):
        texto= "{0}"
        return texto.format(self.nroResidencia)

    class meta:
        verbose_name='Residencia'
        verbose_name_plural='Residencias'
        db_table='residencia'
        ordering=['nroResidencia']

class Correspondencia(models.Model):
    tipo = models.CharField(max_length=30)
    estado = models.CharField(max_length=30, choices=estado)
    residencia= models.ForeignKey(Residencia,null=True,blank=True, on_delete=models.CASCADE)


