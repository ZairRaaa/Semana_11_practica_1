# Práctica 1 · Django

Aplicación de catálogo para la Semana 11 de Desarrollo de Aplicaciones Web.
Python 3.11+ y Django 5.2, con SQLite y arquitectura MTV.

## Ejecutar en PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py poblar_productos
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py runserver
```

Abrir <http://127.0.0.1:8000/>. No es necesario activar el entorno virtual.
El servidor usa `DEBUG=True` únicamente para esta práctica local.
La base de datos y el entorno virtual quedan excluidos de Git.

## Entrega

- [Repositorio de GitHub](https://github.com/ZairRaaa/Semana_11_practica_1).
- [Guía de la práctica](info.md).
- [Evidencias y asistencia de IA](evidencias/README.md).
- [Documentación oficial de Django](https://docs.djangoproject.com/en/5.2/).

## Qué incluye

- Inicio con una vista basada en función y catálogo con `ListView`.
- Rutas con nombres, plantillas con herencia, bloques, etiquetas y filtros.
- Modelo `Producto`, migración y datos de ejemplo reproducibles mediante el ORM.
- Búsqueda por nombre y filtro de disponibilidad, combinables.
- Pruebas: `.\.venv\Scripts\python.exe manage.py test`.

`poblar_productos` puede repetirse: no duplica ni sobrescribe productos existentes.
No hay formulario de compra; el alcance de esta práctica es consultar el catálogo.

## Consultas del ejercicio

Abrir `.\.venv\Scripts\python.exe manage.py shell` y ejecutar:

```python
from catalogo.models import Producto
Producto.objects.all()
Producto.objects.filter(disponible=True)
Producto.objects.filter(precio__lte=20)
```

Los QuerySets se evalúan al recorrerlos o convertirlos en lista; su creación
no ejecuta de inmediato la consulta. El modelo contiene los filtros reutilizables;
la vista recibe la solicitud y la plantilla presenta los resultados.
