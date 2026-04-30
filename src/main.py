import tkinter as tk
from tkinter import filedialog, messagebox
from core.organizador import organizar_archivos
from utils.miscelan import centrar_ventana
from config.tema import obtener_tema

# -------- FUNCIONES --------

tema = obtener_tema(modo_oscuro=True)

def seleccionar_carpeta():
    ruta = filedialog.askdirectory()
    if ruta:
        entrada_ruta.delete(0, tk.END)
        entrada_ruta.insert(0, ruta)

def ejecutar():
    ruta = entrada_ruta.get()
    if ruta:
        organizar_archivos(ruta)
        messagebox.showinfo("Completado", "Archivos organizados correctamente")

# TKRAISE: Permite mostrar un frame específico en un contenedor, ocultando los demás.
def mostrar_inicio():
    frame_inicio.tkraise()

def mostrar_config():
    frame_config.tkraise()

# -------- VENTANA --------

ventana = tk.Tk()
ventana.title("Organizador de Ficheros")

ventana.overrideredirect(True)

ventana.attributes("-alpha", 0.95)

top = tk.Toplevel(ventana)
top.overrideredirect(True)
centrar_ventana(top, 1276, 913)
# -------- BARRA PERSONALIZADA --------

barra = tk.Frame(ventana, bg=tema["panel"], height=30)
barra.grid(row=0, column=0, columnspan=2, sticky="nsew")

titulo = tk.Label(barra, text="Mi aplicación", bg=tema["panel"], fg="white")
titulo.pack(side="left", padx=10)

btn_cerrar = tk.Button(barra, text="X", bg=tema["boton_cancel"], fg="white",
                       command=ventana.destroy, bd=0)
btn_cerrar.pack(side="right")

def click_barra(event):
    ventana.x = event.x
    ventana.y = event.y
    top.x = event.x
    top.y = event.y
    
def mover(event):
    x = event.x_root - ventana.x
    y = event.y_root - ventana.y
    ventana.geometry(f"+{x}+{y}")
    x = event.x_root - top.x
    y = event.y_root - top.y
    top.geometry(f"+{x}+{y}")

barra.bind("<Button-1>", click_barra)
barra.bind("<B1-Motion>", mover)

ventana.configure(bg=tema["fondo"])

centrar_ventana(ventana, 1276, 913)

# Entendiendo Grid
# (0,0) | (0,1)
# ------+------
# (1,0) | (1,1)
# En este caso, el menú estará en (1,0) y el contenedor principal en (1,1)
# Weight: Es la proporción de espacio que cada fila o columna ocupará. Si una fila tiene weight=1 y otra weight=2, 
# la segunda ocupará el doble de espacio que la primera.

# Layout principal con grid
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_rowconfigure(1, weight=8)
ventana.grid_columnconfigure(0, weight=7) 
ventana.grid_columnconfigure(1, weight=12)

# -------- MENÚ IZQUIERDA --------

menu = tk.Frame(ventana, bg=tema["panel"])
menu.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
menu.grid_propagate(False)

btn_inicio = tk.Button(menu, text="Inicio", fg=tema["texto"], bg=tema["panel_titulo"],
                       bd=0, command=mostrar_inicio)
btn_inicio.pack(fill="x", pady=10)

btn_config = tk.Button(menu, text="Configuración", fg=tema["texto"], bg=tema["panel_titulo"],
                       bd=0, command=mostrar_config)
btn_config.pack(fill="x", pady=10)

# -------- CONTENEDOR DERECHO --------

contenedor = tk.Frame(ventana, bg=tema["panel"])
contenedor.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

contenedor.grid_rowconfigure(0, weight=1)
contenedor.grid_columnconfigure(0, weight=1)

# -------- FRAME INICIO --------

frame_inicio = tk.Frame(contenedor, bg=tema["panel"])
frame_inicio.grid(row=0, column=0, sticky="nsew")

titulo = tk.Label(frame_inicio, text="Organizador de Ficheros", font=("Arial", 18), fg=tema["texto"], bg=tema["panel_titulo"])
titulo.pack(pady=20)

entrada_ruta = tk.Entry(frame_inicio, width=50)
entrada_ruta.pack(pady=10)

btn_buscar = tk.Button(frame_inicio, text="Seleccionar carpeta", command=seleccionar_carpeta, fg=tema["texto"], bg=tema["panel_titulo"])
btn_buscar.pack(pady=5)

btn_ejecutar = tk.Button(frame_inicio, text="Organizar", command=ejecutar, fg=tema["texto"], bg=tema["boton_ok"])
btn_ejecutar.pack(pady=20)

# -------- FRAME CONFIG --------

frame_config = tk.Frame(contenedor)
frame_config.grid(row=0, column=0, sticky="nsew")

label_config = tk.Label(frame_config, text="Configuración", font=("Arial", 18))
label_config.pack(pady=20)

# -------- INICIO POR DEFECTO --------

frame_inicio.tkraise()

ventana.mainloop()