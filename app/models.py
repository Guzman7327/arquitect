# app/models.py

from django.db import models

class Videojuego(models.Model):
    nombre = models.CharField(max_length=255)
    plataforma = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.TextField()
    imagen = models.URLField()
    fecha_lanzamiento = models.DateField()
    categoria = models.CharField(max_length=255)  # Asegúrate de que este campo exista

    def __str__(self):
        return self.nombre
