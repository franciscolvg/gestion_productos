from django.db import models

# Create your models here.


class Producto(models.Model):
    TIPO_CHOICES = [
        ('local', 'Local'),
        ('internacional', 'Internacional'),
    ]
    codigo = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    def __str__(self):
        return self.descripcion

