import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from tkinter import messagebox

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.botonPresionado = False
        from pagina_1 import Page1
        from pagina_2 import Page2
        from pagina_3 import Page3
        url_imagen = "https://astelus.com/wp-content/viajes/las-principales-aerolineas-del-mundo.jpg"

        try:
            response = requests.get(url_imagen)
            response.raise_for_status()  # Verificar si hubo errores en la descarga
            imagen_bytes = BytesIO(response.content)
            imagen = Image.open(imagen_bytes)

            imagen = imagen.resize((1500, 1100), Image.LANCZOS)

            global imagen_tk
            imagen_tk = ImageTk.PhotoImage(imagen)

            fondo = tk.Label(self, image=imagen_tk)
            fondo.place(relwidth=1, relheight=1)
        except requests.exceptions.RequestException as e:

            messagebox.showerror("Error a la hora de exportar")

        etiqueta_bienvenida = tk.Label(self, text="¡Bienvenido a la Aerolínea Vuelo Rápido!", font=("Arial", 16),
                                       bg='blue', fg='white')
        etiqueta_bienvenida.pack(pady=20)

        boton1 = tk.Button(self, text="1- Introducir los nodos", command=lambda : controller.show_frame(Page1), width=40, borderwidth=3,
                           relief="ridge")
        boton2 = tk.Button(self, text="2- Diseño del Árbol", command= lambda: controller.show_frame(Page2), width=40, borderwidth=3,
                           relief="ridge")
        boton3 = tk.Button(self, text="3- Representación (gráfica) de Recorridos (vuelos)", command = lambda: controller.show_frame(Page3), width=40, borderwidth=3,
                           relief="ridge")


        boton4 = tk.Button(self, text="Salir", command= lambda: self.detectarBoton(parent),
                           width=40,
                           borderwidth=3, relief="ridge")



        boton1.pack(pady=10)
        boton2.pack(pady=10)
        boton3.pack(pady=10)
        boton4.pack(pady=10)

    def detectarBoton(self, parent):
        self.botonPresionado = True
        if self.botonPresionado:
            parent.destroy()
            parent.quit()
