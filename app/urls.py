from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo, name='catalogo'),
    path('videojuego/<int:id>/', views.detalle_videojuego, name='detalle_videojuego'),
]
