from django.urls import path

from . import views

app_name = "catalogo"

urlpatterns = [
    path("", views.home, name="home"),
    path("catalogo/", views.catalogo, name="lista"),
]
