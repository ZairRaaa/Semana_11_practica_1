from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView

from .models import Producto


def home(request):
    return render(request, "catalogo/home.html", {
        "titulo": "Mi catálogo",
        "fecha": timezone.localdate(),
    })


class ProductoListView(ListView):
    template_name = "catalogo/catalogo.html"
    context_object_name = "productos"
    model = Producto

    def get_queryset(self):
        productos = Producto.objects.all().buscar(self.request.GET.get("q", ""))
        if self.request.GET.get("disponibles") == "1":
            productos = productos.disponibles()
        return productos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Catálogo de productos"
        context["fecha"] = timezone.localdate()
        context["busqueda"] = self.request.GET.get("q", "").strip()
        context["solo_disponibles"] = self.request.GET.get("disponibles") == "1"
        return context
