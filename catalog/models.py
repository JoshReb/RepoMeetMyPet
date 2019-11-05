from django.db import models
from django.urls import reverse

class Tipo(models.Model):
    descripcion_tipo = models.CharField(max_length=250)

    def __str__(self):
        return self.descripcion_tipo

class Mascota(models.Model):
    nombre = models.CharField(max_length=250)
    #tipo = models.ForeignKey(Tipo, on_delete='models.CASCADE')
    tipo = models.ForeignKey('Tipo', on_delete=models.SET_NULL, null=True)
    raza = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=500)
    foto = models.FileField(default='catalog\static\catalog\images\back.jpg')

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.nombre