import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
from datetime import datetime
import networkx as nx
import matplotlib.pyplot as plt
def generar_grafo_arbol(arbol):
    G = nx.DiGraph()

    def agregar_nodo_y_conexiones(nodo, index, x, y):
        if nodo:
            label = f"Destino: {nodo.destino}\nFecha: {nodo.fecha}"
            G.add_node(index, label=label, pos=(x, y))
            if nodo.vuelo1:
                G.add_edge(index, index * 2)
                agregar_nodo_y_conexiones(nodo.vuelo1, index * 2, x - 1, y - 1)
            if nodo.vuelo2:
                G.add_edge(index, index * 2 + 1)
                agregar_nodo_y_conexiones(nodo.vuelo2, index * 2 + 1, x + 1, y - 1)

    agregar_nodo_y_conexiones(arbol.raiz, 1, 0, 0)  # Empieza en la raíz en la posición (0, 0)
    pos = nx.get_node_attributes(G, 'pos')  # Obtener posiciones de los nodos
    return G, pos

class NodoVuelo:
    def __init__(self, destino, fecha, asientos):
        self.destino = destino
        self.fecha = fecha
        self.asientos = asientos
        self.vuelo1 = None
        self.vuelo2 = None

class ArbolVuelos:
    def __init__(self):
        self.raiz = None

    # Implementa la lógica para insertar nodos en el árbol binario.
    def insertar(self, destino, fecha, asientos):
        if not self.raiz:
            self.raiz = NodoVuelo(destino, fecha, asientos)
        else:
            self._insertar_recursivo(self.raiz, destino, fecha, asientos)

    def _insertar_recursivo(self, nodo_actual, destino, fecha, asientos):
        if fecha < nodo_actual.fecha:
            if nodo_actual.vuelo1 is None:
                nodo_actual.vuelo1 = NodoVuelo(destino, fecha, asientos)
            else:
                self._insertar_recursivo(nodo_actual.vuelo1, destino, fecha, asientos)
        else:
            if nodo_actual.vuelo2 is None:
                nodo_actual.vuelo2 = NodoVuelo(destino, fecha, asientos)
            else:
                self._insertar_recursivo(nodo_actual.vuelo2, destino, fecha, asientos)


arbol_vuelos = None
def crear_y_mostrar_arbol():
    global arbol_vuelos
    arbol_vuelos = ArbolVuelos()

    # Inserta los vuelos registrados en el árbol
    for destino, fecha, asientos, in vuelos_registrados:
        arbol_vuelos.insertar(destino, fecha, asientos)
    print(arbol_vuelos.raiz.fecha)
# Lista para almacenar los vuelos registrados
vuelos_registrados = []

def crear_y_mostrar_design():

    if arbol_vuelos is None:
        messagebox.showinfo("Usted necesita generar nodos para mostrar")
    elif arbol_vuelos.raiz is None:
        messagebox.showinfo("Disculpe, no existen nodos en este arbol")
    else:
        # Genera el grafo del árbol binario
        G, pos = generar_grafo_arbol(arbol_vuelos)


        # Obtener etiquetas de nodos
        labels = {n: data["label"] for n, data in G.nodes(data=True)}

        # Dibujar el grafo
        nx.draw(G, pos, labels=labels, with_labels=True, node_size=2000, node_color="green", font_size=10)

        # Mostrar el gráfico utilizando Matplotlib

        plt.axis("off")
        plt.show()



def opcion1():
    def guardar_nodos():
        destino = destino_entry.get()
        fecha_str = fecha_entry.get()
        asientos = asientos_entry.get()


        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")  # Convierte la cadena a un objeto de fecha
            fecha_formateada = fecha.strftime("%d/%m/%Y")  # Formatea la fecha nuevamente como cadena

            # Agrega el destino y la fecha formateada a la lista de vuelos registrados
            vuelos_registrados.append((destino, fecha_formateada, asientos))

            # Limpia los campos de entrada
            destino_entry.delete(0, tk.END)
            fecha_entry.delete(0, tk.END)


        except ValueError:
            messagebox.showerror("Error", "Fecha no válida. Utilice el formato %d/%m/%Y")

    def mostrar_vuelos_registrados():
        if vuelos_registrados:
            ventana_vuelos = tk.Toplevel(
                ventana)  # Crea una nueva ventana emergente para mostrar los vuelos registrados
            ventana_vuelos.title("Vuelos Registrados")

            tk.Label(ventana_vuelos, text="Destino", font=("Arial", 12, "bold")).grid(row=0, column=0)
            tk.Label(ventana_vuelos, text="Fecha", font=("Arial", 12, "bold")).grid(row=0, column=1)

            # Muestra los vuelos registrados en la nueva ventana
            for i, (destino, fecha, asientos) in enumerate(vuelos_registrados, start=1):
                tk.Label(ventana_vuelos, text=destino).grid(row=i, column=0)
                tk.Label(ventana_vuelos, text=fecha).grid(row=i, column=1)
                tk.Label(ventana_vuelos, text=asientos).grid(row=i, column=2)
        else:
            messagebox.showinfo("Información", "No hay vuelos registrados.")

    ventana_nodos = tk.Toplevel(ventana)  # Crea una nueva ventana emergente
    ventana_nodos.title("Introducir Nodos")

    # Agrega etiquetas y campos de entrada para destinos y fechas
    tk.Label(ventana_nodos, text="Destino:").pack()
    destino_entry = tk.Entry(ventana_nodos)
    destino_entry.pack()

    tk.Label(ventana_nodos, text="Fecha (%d/%m/%Y):").pack()
    fecha_entry = tk.Entry(ventana_nodos)
    fecha_entry.pack()

    tk.Label(ventana_nodos, text="Asientos:").pack()
    asientos_entry = tk.Entry(ventana_nodos)
    asientos_entry.pack()

    tk.Button(ventana_nodos, text="Guardar", command=guardar_nodos).pack()
    tk.Button(ventana_nodos, text="Mostrar Vuelos Registrados", command=mostrar_vuelos_registrados).pack()


def opcion2():
    nueva_ventana = tk.Toplevel(ventana)
    label_crear_design = tk.Label(nueva_ventana, text="Presione el boton para generar el diseño de árbol")
    label_crear_design.pack()
    boton_crear_arbol = tk.Button(nueva_ventana, text="Cree el árbol" , command=lambda : crear_y_mostrar_arbol())
    boton_crear_arbol.pack()


def opcion3():
   nueva_ventana = tk.Toplevel(ventana)
   label_crear_design = tk.Label(nueva_ventana, text="Genere la representación gráfica del árbol")
   label_crear_design.pack()
   boton_crear_representacion = tk.Button(nueva_ventana, text="Genere la representación", command=lambda : crear_y_mostrar_design())
   boton_crear_representacion.pack()


def opcion4():
    ventana.quit()


def configurar_ventana():
    ventana.title("BIENVENIDO A LA AEROLÍNEA VUELO RÁPIDO")
    ventana.geometry("400x300")

    url_imagen = "https://astelus.com/wp-content/viajes/las-principales-aerolineas-del-mundo.jpg"
    try:
        response = requests.get(url_imagen)
        response.raise_for_status()  # Verificar si hubo errores en la descarga
        imagen_bytes = BytesIO(response.content)
        imagen = Image.open(imagen_bytes)

        imagen = imagen.resize((1500, 1100), Image.LANCZOS)

        global imagen_tk
        imagen_tk = ImageTk.PhotoImage(imagen)

        fondo = tk.Label(ventana, image=imagen_tk)
        fondo.place(relwidth=1, relheight=1)
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", "Error al descargar la imagen:\n{}".format(e))

    etiqueta_bienvenida = tk.Label(ventana, text="¡Bienvenido a la Aerolínea Vuelo Rápido!", font=("Arial", 16),
                                   bg='blue', fg='white')
    etiqueta_bienvenida.pack(pady=20)

    boton1 = tk.Button(ventana, text="1- Introducir los nodos", command=opcion1, width=40, borderwidth=3,
                       relief="ridge")
    boton2 = tk.Button(ventana, text="2- Diseño del Árbol", command=opcion2, width=40, borderwidth=3, relief="ridge")
    boton3 = tk.Button(ventana, text="3- Representación (gráfica) de Recorridos (vuelos)", command=opcion3, width=40,
                       borderwidth=3, relief="ridge")
    boton4 = tk.Button(ventana, text="4- Salir", command=opcion4, width=40, borderwidth=3, relief="ridge")

    boton1.pack(pady=10)
    boton2.pack(pady=10)
    boton3.pack(pady=10)
    boton4.pack(pady=10)


if __name__ == "__main__":
    ventana = tk.Tk()
    configurar_ventana()
    ventana.mainloop()
