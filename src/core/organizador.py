import os
import shutil
from config.extensiones import extensiones

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