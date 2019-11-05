#Intento de pruebas segun video
from django.test import TestCase

# Create your tests here.
from models import Mascota
import unittest

class MascotaModelTest(unittest.TestCase):
    @classmethod
    def setUpTestData(cls):
        Mascota.objects.create(descripcion='esto es una prueba')

    def test_descripcion_max_length(self):
        mascota = Mascota.objects.get(id=1)
        max_length= mascota._meta.get_field('descripcion').max_length
        self.assertEquals(max_length, 500)