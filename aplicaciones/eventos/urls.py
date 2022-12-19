from django.urls import path
from .views import *

urlpatterns = [
    path('agregar/', agregar, name='agregar_evento'),
    path('listado/', listado, name='listado_eventos'),
]
