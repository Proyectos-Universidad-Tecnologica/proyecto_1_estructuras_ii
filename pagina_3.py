import tkinter as tk
from  tkinter import  ttk


LARGEFONT = ("Verdana", 35)
class Page3(tk.Frame):
    def __init__(self, parent, controller):
        from pagina_inicio import StartPage
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 3", font=LARGEFONT)
        label.pack()

        button2 = ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.pack()