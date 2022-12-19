from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eventos/', include('aplicaciones.eventos.urls')),
    path('noticias/', include('aplicaciones.noticias.urls')),
    path('', inicio, name='inicio'),
    path('inicio/', inicio, name='inicio'),
    path('sobre_nosotros/', sobre_nosotros, name='sobre_nosotros'),
    path('contacto/', contacto, name='contacto'),
    path('registrar/', registrar, name='registrar'),
    path('ingresar/', ingresar, name='ingresar'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
