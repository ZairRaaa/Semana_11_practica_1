
GUÍA PRÁCTICA SEMANA 11
Asignatura: Desarrollo de Aplicaciones Web (IS093A)
Unidad II: Desarrollo Web Fullstack
Tema: Introducción a Django: Arquitectura MTV, URLs, Vistas (FBV/CBV), Plantillas (Herencia, Bloques, Tags, Filtros) y Modelos (ORM,  Consultas)
Modalidad: Presencial / Laboratorio
Fecha: 17.06.2026
Duración: 60 minutos
APELLIDOS Y NOMBRES:  	

OBJETIVO DE LA PRÁCTICA
Construir una aplicación web funcional con Django 5.x, aplicando el patrón MTV (Model-Template-View), configurando enrutamiento con urls.py, desarrollando vistas basadas en funciones (FBV) y clases (CBV), implementando plantillas con herencia, bloques, etiquetas y filtros, y definiendo modelos con el ORM de Django para persistencia en SQLite. Validar el ciclo solicitud-respuesta, la migración de base de datos y preparar la estructura para formularios, admin y sesiones (Semana 12).
RECURSOS REQUERIDOS
•	Python 3.11+ + pip
•	Visual Studio Code (Extensiones: Python, Django, SQLite Viewer, Pylint)
•	Terminal integrada + entorno virtual (venv)
•	Navegador moderno + DevTools
•	Documentación oficial: docs.djangoproject.com/en/5.0/
•	Conexión a internet + GitHub PARTE 1: EJERCICIO PASO A PASO

Paso	
Actividad	
Tiempo aprox.	
Concepto Clave	
Restricción/Nota Técnica

1	
Crear entorno virtual, instalar Django, iniciar proyecto (startproject) y app (startapp). Verificar	
5 min	
MTV vs MVC,
aislamiento de entornos, manage.py como orquestador	
No modificar settings.py innecesariamente. Verificar INSTALLED_APPS
 

	runserver y estructura de carpetas			

2	
Configurar rutas: app/urls.py, incluirla en project/urls.py.
Mapear path() a vistas. Usar name para reversibilidad	
8 min	
Routing, desacoplamiento de apps, include(), resolución de URLs	
Prohibido hardcodear URLs en templates.
Usar {% url 'nombre'
%}

3	
Implementar vistas: 1 FBV (def home) y 1 CBV (ListView).
Retornar HttpResponse o render(). Pasar contexto	
10 min	
Request/Response cycle, render(), ListView, get_context_data()	
Evitar lógica de negocio en vistas. Delegar a modelos o servicios

4	
Crear plantillas: base.html con bloques, catalogo.html con {% extends %}, {% for
%}, {% if %}, filtros (`title, date`)	
10 min		

5	
Definir modelo Producto, ejecutar makemigrations y migrate. Poblar datos, consultar con objects.all() y filter()	
12 min	
ORM, migraciones, QuerySets (lazy evaluation),    str 	 	
Verificar python manage.py check antes de runserver. Nunca commitear db.sqlite3
 

USO CONTROLADO DE HERRAMIENTAS DE IA


Herramienta	
Uso Permitido	
Prompt Ejemplo	
Uso Prohibido

ChatGPT/Claude/Copilot	
Explicar diferencia FBV vs CBV, depurar TemplateDoesNotExist, generar querysets básicos	
"¿Por quéListViewno renderiza mis objetos y cómo verificarobject_listen el contexto?"	
"Genera la app Django completa con vistas, templates y modelos"

Django Docs / manage.py	
Validar sintaxis de tags/filtros, revisar migraciones, ejecutar shell_plus	
(Oficial)	
Ignorar advertencias de Unapplied migrations o DEBUG=True en logs

SQLite Viewer / dbshell	
Inspeccionar tablas, verificar datos insertados, depurar IntegrityError	
(Automático)	
Modificar db.sqlite3 manualmente sin usar ORM

     Regla de laboratorio: El 75% de la configuración MTV, vistas y templates debe escribirse manualmente. Cada uso de IA para resolver errores de rutas, ORM o renderizado debe llevar # IA: [problema] → Solución manual:  [explicación].
Evidencias del Ejercicio Desarrollado:
•	Añada capturas de pantalla de cada paso realizado.
•	Proporcione el enlace de Github de su proyecto
