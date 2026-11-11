from django.db import models
from django.core.validators import MinValueValidator


class ProductoQuerySet(models.QuerySet):
    def buscar(self, termino):
        return self.filter(nombre__icontains=termino.strip()) if termino.strip() else self

    def disponibles(self):
        return self.filter(disponible=True)


class Producto(models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])
    disponible = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    objects = ProductoQuerySet.as_manager()

    class Meta:
        ordering = ["nombre"]
        constraints = [
            models.CheckConstraint(condition=models.Q(precio__gte=0), name="producto_precio_no_negativo"),
        ]

    def __str__(self):
        return self.nombre
