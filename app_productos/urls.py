from django.urls import path
from .views import lista_productos, registrar_producto, productos_api

urlpatterns = [
    path('api/productos/', productos_api, name='productos_api'),
    path('listar/', lista_productos, name='lista_productos'),
    path('registrar/', registrar_producto, name='registrar_producto'),
]
