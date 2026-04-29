import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Tipos de archivos
extensiones = {
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Otros": []
}

def organizar_archivos(ruta):
    contador = 0
    # Crear carpetas si no existen
    for carpeta in extensiones.keys():
        os.makedirs(os.path.join(ruta, carpeta), exist_ok=True)

    # Recorrer archivos
    for archivo in os.listdir(ruta):
        ruta_archivo = os.path.join(ruta, archivo)

        if os.path.isfile(ruta_archivo):
            extension = os.path.splitext(archivo)[1].lower()
            movido = False

            for carpeta, exts in extensiones.items():
                destino = os.path.join(ruta, carpeta, archivo)

                if extension in exts:
                    print(f"Moviendo {archivo} -> {carpeta}")
                    if not os.path.exists(destino):
                        shutil.move(ruta_archivo, destino)
                        movido = True
                        break
                    else:
                        print(f"Archivo ya existe: {archivo}")
                    

            if not movido:
                print(f"Moviendo {archivo} -> Otros")
                shutil.move(ruta_archivo, os.path.join(ruta, "Otros", archivo))
            
            contador += 1

    print(f"Total de archivos movidos: {contador}")

    print("Organización completada.")

def centrar_ventana(ventana, ancho, alto):
    # Obtener dimensiones de la pantalla
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()

    # Calcular posiciones x e y
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)

    # Establecer la geometría
    ventana.geometry(f'{ancho}x{alto}+{x}+{y}')

# Función botón
def ejecutar():
    ruta = filedialog.askdirectory()
    if ruta:
        organizar_archivos(ruta)
        messagebox.showinfo("Completado", "Archivos organizados correctamente")

# Interfaz
ventana = tk.Tk()
ventana.title("Organizador de Ficheros")
#ventana.geometry("600x300")

centrar_ventana(ventana, 600, 300)

titulo = tk.Label(ventana, text="Organizador de Ficheros", font=("Arial", 14))
titulo.pack(pady=40)

boton = tk.Button(ventana, text="Actualizar / Organizar", command=ejecutar)
boton.pack(pady=70)

ventana.mainloop()