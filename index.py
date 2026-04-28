import os
import shutil

# Ruta a organizar (cámbiala)
ruta = "C:/Users/jbenitez/Downloads"

# Tipos de archivos
extensiones = {
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Otros": []
}

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
            if extension in exts:
                shutil.move(ruta_archivo, os.path.join(ruta, carpeta, archivo))
                movido = True
                break

        if not movido:
            shutil.move(ruta_archivo, os.path.join(ruta, "Otros", archivo))

print("Organización completada.")