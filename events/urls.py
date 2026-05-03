from django.urls import path
from .views import lista_servicios, crear_servicio

urlpatterns = [
    path('', lista_servicios, name='lista_servicios'),
    path('crear/', crear_servicio, name='crear_servicio'),
]