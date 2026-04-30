
def centrar_ventana(ventana, ancho, alto):
    # Obtener dimensiones de la pantalla
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()

    # Calcular posiciones x e y
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)

    # Establecer la geometría
    ventana.geometry(f'{ancho}x{alto}+{x}+{y}')