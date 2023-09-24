
import tkinter as tk
from tkinter import ttk
import datetime

LARGEFONT = ("Verdana", 35)

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        from pagina_inicio import StartPage
        label = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label.pack()

        button2 = ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.pack()
