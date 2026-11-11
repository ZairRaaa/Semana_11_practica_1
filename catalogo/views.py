from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Mi catálogo</h1><p>La ruta de inicio funciona.</p>")


def catalogo(request):
    return HttpResponse("<h1>Catálogo</h1><p>La ruta del catálogo funciona.</p>")
