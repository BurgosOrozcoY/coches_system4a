from tkinter import Tk
from views.coches_view import CochesView

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestion de Coches")
        self.ventana.geometry("600x600")
        self.ventana.resizable(0,0)
        self.view = CochesView(self.ventana)
        self.view.main()
        #self.main()


if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()