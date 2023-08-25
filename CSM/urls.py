"""
Configuración de las URL para el proyecto Django.

Este módulo define las URL principales del proyecto y su correspondencia con las vistas.
Utiliza el enrutamiento de Django para asociar las rutas URL con las vistas apropiadas.

URLs incluidas:
- 'admin/': Ruta para acceder a la interfaz de administración de Django.
- '': Ruta raíz que incluye las URLs definidas en el módulo 'home.urls'.
- 'accounts/': Ruta para gestionar las funcionalidades de autenticación utilizando 'allauth.urls'.

Este archivo define la lista 'urlpatterns', que es utilizada por Django para enrutar las solicitudes URL a las vistas correspondientes.

Detalles de las vistas y funcionalidades están definidos en otros módulos y aplicaciones.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('allauth.urls')),
]
