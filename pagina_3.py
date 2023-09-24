import tkinter as tk
from  tkinter import  ttk
import matplotlib as plt

LARGEFONT = ("Verdana", 35)
class Page3(tk.Frame):
    def __init__(self, parent, controller):
        from pagina_inicio import StartPage
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 3", font=LARGEFONT)
        label.pack()

        self.representacion_grafica()
        button2 = ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.pack()

    def representacion_grafica(self, root):
        # Crear una figura de Matplotlib
        fig, ax = plt.subplots()
        self._representacion_grafica_recursiva(root, ax, fig, 0, 0)

        # Mostrar la figura
        plt.show()

    def _representacion_grafica_recursiva(self, nodo, ax, fig, x, y):
        if nodo is not None:
            # Dibuja el nodo
            ax.text(x, y, f"{nodo.destino}\n{str(nodo.fecha)}", ha="center", va="center",
                    bbox=dict(facecolor="white", edgecolor="black"))

            # Dibuja la conexión con el vuelo 1
            if nodo.vuelo1:
                ax.plot([x, x - 1], [y - 1, y - 2], "b-")
                self._representacion_grafica_recursiva(nodo.vuelo1, ax, fig, x - 1, y - 2)

            # Dibuja la conexión con el vuelo 2
            if nodo.vuelo2:
                ax.plot([x, x + 1], [y - 1, y - 2], "b-")
                self._representacion_grafica_recursiva(nodo.vuelo2, ax, fig, x + 1, y - 2)
