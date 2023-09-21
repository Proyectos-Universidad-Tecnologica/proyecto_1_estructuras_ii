import tkinter as tk
from pagina_inicio import StartPage
from pagina_1 import Page1
from pagina_2 import Page2
from pagina_3 import Page3

class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk

        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        frame = StartPage(container, self)
        frame_1 = Page1(container, self)
        frame_2 = Page2(container, self)
        frame_3 = Page3(container, self)
        self.frames = {}

        self.frames[StartPage] = frame
        self.frames[Page1] = frame_1
        self.frames[Page2] = frame_2
        self.frames[Page3] = frame_3

        frame.grid(row=0, column=0, sticky="nsew")
        frame_1.grid(row=0, column=0, sticky="nsew")
        frame_2.grid(row=0, column=0, sticky="nsew")
        frame_3.grid(row=0, column=0, sticky="nsew")

        container.pack(side="top", fill="both", expand=True)
        self.title("BIENVENIDO A LA AEROLÍNEA VUELO RÁPIDO")
        self.geometry("400x300")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


app = tkinterApp()
app.mainloop()