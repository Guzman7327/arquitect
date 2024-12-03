from django.shortcuts import render
from .models import Videojuego

def catalogo(request):
    # Obtener todos los videojuegos
    juegos_populares = Videojuego.objects.filter(categoria="Juegos Populares")
    nuevos_lanzamientos = Videojuego.objects.filter(categoria="Nuevo Lanzamiento")

    # Pasar ambas categorías a la plantilla
    return render(request, 'index.html', {
        'juegos_populares': juegos_populares,
        'nuevos_lanzamientos': nuevos_lanzamientos
    })

def detalle_videojuego(request, id):
    try:
        videojuego = Videojuego.objects.get(id=id)
    except Videojuego.DoesNotExist:
        return render(request, '404.html')  # Si no se encuentra, mostrar un 404
    return render(request, 'diseño.html', {'videojuego': videojuego})



