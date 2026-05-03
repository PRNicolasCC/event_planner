from django.db import models
from django.conf import settings


class Servicio(models.Model):
    proveedor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)

    precio_referencia = models.DecimalField(max_digits=10, decimal_places=2)
    telefono_contacto = models.CharField(max_length=20)

    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre