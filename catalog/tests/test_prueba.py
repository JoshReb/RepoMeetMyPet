#Intento de pruebas segun PDF
from  django.test import TestCase
from catalog.models import Mascota

class MascotaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Mascota.objects.create(descripcion='esto es una prueba')

    #Verifica que el largo maximo del atributo este configurado a 500 caracteres
    def test_descripcion_max_length(self):
        mascota = Mascota.objects.get(id=1)
        max_length= mascota._meta.get_field('descripcion').max_length
        self.assertEquals(max_length, 500)

    #Verifica que el url corresponda a lo deseado
    def test_get_absolute_url(self):
        mascota = Mascota.objects.get(id=1)
        self.assertEquals(mascota.get_absolute_url(),'/catalog/mascota/1')


        
