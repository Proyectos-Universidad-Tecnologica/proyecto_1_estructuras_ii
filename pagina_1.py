import tkinter as tk
from tkinter import ttk

LARGEFONT = ("Verdana", 35)
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        from pagina_inicio import StartPage
        label = ttk.Label(self, text="Page 1", font=LARGEFONT)
        label.pack()

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="StartPage",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

