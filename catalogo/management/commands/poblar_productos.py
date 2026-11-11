from decimal import Decimal

from django.core.management.base import BaseCommand
from django.db import transaction

from catalogo.models import Producto


class Command(BaseCommand):
    help = "Agrega seis productos de ejemplo sin duplicar ni sobrescribir los existentes."

    @transaction.atomic
    def handle(self, *args, **options):
        ejemplos = [
            ("cuaderno de puntos", "80 hojas para apuntes, bocetos y nuevas ideas.", "18.90", True),
            ("lápices de grafito", "Set de 6 lápices para escribir y dibujar.", "12.50", True),
            ("marcadores pastel", "Seis colores suaves para destacar lo esencial.", "24.00", True),
            ("organizador de escritorio", "Un espacio para cada una de tus herramientas.", "35.90", False),
            ("planificador semanal", "Organiza tus proyectos, una semana a la vez.", "22.00", True),
            ("regla metálica", "30 centímetros de precisión para tus trazos.", "9.90", True),
        ]
        creados = 0
        for nombre, descripcion, precio, disponible in ejemplos:
            _, nuevo = Producto.objects.get_or_create(
                nombre=nombre,
                defaults={"descripcion": descripcion, "precio": Decimal(precio), "disponible": disponible},
            )
            creados += nuevo
        self.stdout.write(self.style.SUCCESS(f"Productos nuevos: {creados}. Total: {Producto.objects.count()}."))
