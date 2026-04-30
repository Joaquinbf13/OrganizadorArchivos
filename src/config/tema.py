# COLORES PARA EL TEMA OSCURO Y CLARO
def rgb(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"

def obtener_tema(modo_oscuro=True):

    if modo_oscuro:
        return {
            "texto": "white",
            "texto_descriptivo": rgb(180, 180, 180),

            "fondo": rgb(32, 32, 32),
            "panel_titulo": rgb(45, 45, 45),
            "panel_subtitulo": rgb(60, 60, 60),
            "panel": rgb(30, 30, 30),

            "boton_ok": rgb(0, 102, 255),
            "boton_cancel": rgb(255, 22, 22)
        }
    else:
        return {
            "texto": "black",
            "texto_descriptivo": rgb(75, 75, 75),

            "fondo": "#f0f0f0",
            "panel_titulo": rgb(230, 230, 230),
            "panel_subtitulo": rgb(215, 215, 215),
            "panel": rgb(200, 200, 200),

            "boton_ok": rgb(149, 218, 255),
            "boton_cancel": rgb(255, 149, 149)
        }