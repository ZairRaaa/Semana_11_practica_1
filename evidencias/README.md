# Evidencias de la práctica

Cada etapa conserva su captura real del navegador y un registro de comprobación.
Las capturas muestran el estado de la aplicación al cerrar ese avance.

## 1. Entorno y proyecto

- Creo el entorno virtual e instalo Django 5.2.
- Inicio el proyecto `config` y la aplicación `catalogo`.
- Registro la aplicación y aplico las migraciones iniciales de Django.
- Verifico el proyecto antes de iniciar el servidor local.
- Captura: `01-proyecto.jpg`.

## 2. Rutas de la aplicación

- Conecto `catalogo.urls` mediante `include()` y nombro las rutas.
- Compruebo `reverse()`, `resolve()` y las respuestas HTTP de inicio y catálogo.
- Captura: `02-rutas.jpg`.

## 3. Vistas y contexto

- Implemento `home` como FBV con `render()`.
- Implemento `ProductoListView` y agrego título y fecha con `get_context_data()`.
- Uso temporalmente una lista vacía hasta definir el modelo del paso 5.
- Captura: `03-vistas.jpg`.

## Registro de asistencia

El desarrollo se realiza con asistencia de IA por solicitud del estudiante.
No se declara que el 75 % del código haya sido escrito manualmente.
La guía exige ese porcentaje: el estudiante debe revisar y reproducir el trabajo
manualmente para cumplirlo. Los registros de ejecución corresponden a verificaciones reales.

### Incidencias resueltas con IA

`# IA: DisallowedHost al verificar las vistas en shell → Solución manual: permitir localhost con override_settings únicamente dentro de la comprobación; conservar settings.py sin cambios.`

La solución anterior fue aplicada por IA; se registra como explicación para su revisión
y reproducción manual, no como una intervención manual ya realizada por el estudiante.
