from decimal import Decimal
from io import StringIO

from django.core.exceptions import ValidationError
from django.core.management import call_command
from django.db import IntegrityError, transaction
from django.test import TestCase
from django.urls import reverse

from .models import Producto


class CatalogoTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.cuaderno = Producto.objects.create(nombre="cuaderno azul", precio="18.90", disponible=True)
        Producto.objects.create(nombre="regla", precio="9.90", disponible=False)

    def test_inicio_usa_base_y_contexto(self):
        response = self.client.get(reverse("catalogo:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalogo/base.html")
        self.assertIn("fecha", response.context)
        self.assertContains(response, reverse("catalogo:lista"))

    def test_catalogo_renderiza_productos_y_disponibilidad(self):
        response = self.client.get(reverse("catalogo:lista"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cuaderno Azul")
        self.assertContains(response, "18,90")
        self.assertContains(response, "Agotado")
        self.assertQuerySetEqual(response.context["productos"], Producto.objects.all())

    def test_busqueda_y_disponibilidad_se_combinan(self):
        response = self.client.get(reverse("catalogo:lista"), {"q": " CUADERNO ", "disponibles": "1"})
        self.assertQuerySetEqual(response.context["productos"], [self.cuaderno])
        self.assertEqual(list(Producto.objects.filter(disponible=True)), [self.cuaderno])

    def test_filtro_excluye_agotados(self):
        response = self.client.get(reverse("catalogo:lista"), {"disponibles": "1"})
        self.assertQuerySetEqual(response.context["productos"], [self.cuaderno])
        self.assertNotContains(response, "Agotado")

    def test_busqueda_sin_resultados_escapa_el_texto(self):
        response = self.client.get(reverse("catalogo:lista"), {"q": '<script>alert("x")</script>'})
        self.assertContains(response, "No hay productos para mostrar")
        self.assertNotContains(response, '<script>alert("x")</script>')
        self.assertContains(response, "&lt;script&gt;")

    def test_nombre_legible_y_precio_validado(self):
        self.assertEqual(str(self.cuaderno), "cuaderno azul")
        self.cuaderno.precio = Decimal("-1")
        with self.assertRaises(ValidationError):
            self.cuaderno.full_clean()

    def test_base_de_datos_impide_precio_negativo(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            Producto.objects.create(nombre="precio inválido", precio="-1")

    def test_poblado_repetible_conserva_cambios(self):
        call_command("poblar_productos", stdout=StringIO())
        count = Producto.objects.count()
        producto = Producto.objects.get(nombre="cuaderno de puntos")
        producto.precio = Decimal("20")
        producto.save()
        call_command("poblar_productos", stdout=StringIO())
        self.assertEqual(Producto.objects.count(), count)
        producto.refresh_from_db()
        self.assertEqual(producto.precio, Decimal("20"))
