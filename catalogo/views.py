from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView


def home(request):
    return render(request, "catalogo/home.html", {
        "titulo": "Mi catálogo",
        "fecha": timezone.localdate(),
    })


class ProductoListView(ListView):
    template_name = "catalogo/catalogo.html"
    context_object_name = "productos"
    # En el paso 5 este listado se conectará al modelo Producto.
    queryset = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Catálogo de productos"
        context["fecha"] = timezone.localdate()
        return context
