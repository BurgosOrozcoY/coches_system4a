from coches import coches
from tkinter import *
from tkinter import messagebox

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestion de Coches")
        self.ventana.geometry("600x600")
        self.ventana.resizable(0,0)
        self.main()

    def borrarPantalla(self):
        for witget in self.ventana.winfo_children():
            witget.destroy()

    def menu_acciones(self):
        self.borrarPantalla()
        tipo = "Coches"
        Label(self.ventana, text = f"\n...::: Menu de {tipo} :::...").pack(pady=10)
        Button(self.ventana, text = "1.- Agregar", command = self.insertar_view).pack(pady=5)
        Button(self.ventana, text = "2.- Borrar", command = self.eliminar_view).pack(pady=5)
        Button(self.ventana, text = "3.- Modificar", command = self.modificar_view).pack(pady=5)
        Button(self.ventana, text = "4.- Mostrar", command = self.consultar_view).pack(pady=5)
        Button(self.ventana, text = "5.- Regresar", command = self.main).pack(pady=5)

    def insertar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text = "...Ingresar los datos del coche...").pack(pady = 10)
        Label(self.ventana, text = "Marca:").pack(pady = 5)
        self.marca = Entry(self.ventana)
        self.marca.focus()
        self.marca.pack(pady = 5)
        Label(self.ventana, text = "Color:").pack(pady = 5)
        self.color = Entry(self.ventana)
        
        self.color.pack(pady = 5)
        Label(self.ventana, text = "Modelo:").pack(pady = 5)
        self.modelo = Entry(self.ventana)
        
        self.modelo.pack(pady = 5)
        Label(self.ventana, text = "Velocidad:").pack(pady = 5)
        self.velocidad = Entry(self.ventana)
        
        self.velocidad.pack(pady = 5)
        Label(self.ventana, text = "Potencia:").pack(pady = 5)
        self.potencia = Entry(self.ventana)
        
        self.potencia.pack(pady = 5)
        Label(self.ventana, text = "Asientos:").pack(pady = 5)
        self.asientos = Entry(self.ventana)
        
        self.asientos.pack(pady = 5)
        Button(self.ventana, text = "Guardar", command = lambda: (self.insertar_controller(), self.insertar_view())).pack(pady = 10)
        Button(self.ventana, text = "Regresar", command = self.menu_acciones).pack(pady = 5)

    def eliminar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text = "...Ingresar el ID del coche a eliminar...").pack(pady = 10)
        Label(self.ventana, text = "ID:").pack(pady = 5)
        self.id = Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady = 5)
        self.btn_buscar = Button(self.ventana, text = "Buscar", command= lambda: self.buscar_controller("eliminar"))
        self.btn_buscar.pack(pady = 5)
        self.btn_eliminar = Button(self.ventana, text = "Eliminar", state = "disabled", command= lambda: (self.eliminar_controller(), self.eliminar_view()))
        self.btn_eliminar.pack(pady = 10)
        Button(self.ventana, text = "Regresar", command = self.menu_acciones).pack(pady = 5)

    def modificar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text = "...Ingresar el ID del coche a modificar...").pack(pady = 10)
        Label(self.ventana, text = "ID:").pack(pady = 5)
        self.id = Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady = 5)

        Label(self.ventana, text = "Nueva marca:").pack(pady = 5)
        self.marca = Entry(self.ventana)
        self.marca.pack(pady = 5)
        Label(self.ventana, text = "Nuevo color:").pack(pady = 5)
        self.color = Entry(self.ventana)
        
        self.color.pack(pady = 5)
        Label(self.ventana, text = "Nuevo modelo:").pack(pady = 5)
        self.modelo = Entry(self.ventana)
        
        self.modelo.pack(pady = 5)
        Label(self.ventana, text = "Nueva velocidad:").pack(pady = 5)
        self.velocidad = Entry(self.ventana)
        
        self.velocidad.pack(pady = 5)
        Label(self.ventana, text = "Nueva potencia:").pack(pady = 5)
        self.potencia = Entry(self.ventana)
        
        self.potencia.pack(pady = 5)
        Label(self.ventana, text = "Nuevos Asientos:").pack(pady = 5)
        self.asientos = Entry(self.ventana)
        
        self.asientos.pack(pady = 5)
        Button(self.ventana, text = "Guardar", command = lambda: (self.modificar_controller(), self.modificar_view())).pack(pady = 10)
        Button(self.ventana, text = "Regresar", command = self.menu_acciones).pack(pady = 5)

    def consultar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...Consultar los coches...").pack(pady=10)
        filas = ""
        filas = self.consultar_controller(filas)
        Label(self.ventana, text=f"{filas}").pack(pady=5)
        Button(self.ventana, text= "Regresar", command= self.menu_acciones).pack(pady=5)

    def cambiar_estado_btn(self, estado, tipo_accion):
        if estado:
            if tipo_accion == "eliminar":
                self.btn_eliminar.config(state="normal")
            elif tipo_accion == "modificar":
                self.btn_modificar.config(state="normal")
        else:
            if tipo_accion == "eliminar":
                self.btn_eliminar.config(state="disabled")
            elif tipo_accion == "modificar":
                self.btn_modificar.config(state="disabled")

    def confirmacion_eliminar(self, tipo):
        resp = messagebox.askquestion(title="... Atención ...", message=f"...¿Estas seguro de {tipo} este registro?...") 
        if resp == "yes":
            return True
        else:
            return False

    #   CONTROLADOR del SISTEMA
    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(title="... Exitoso ...", message="...Accion realizada con exito...")
        else:
            messagebox.showerror(title="... Verifica por favor ...", message="...Esta accion no puede realizarse...")

    def insertar_controller(self):
        coche1=coches.Coches(self.marca.get(), self.color.get(), self.modelo.get(), self.velocidad.get(), self.potencia.get(), self.asientos.get())
        respuesta = coche1.insertar()
        self.respuesta_sql(respuesta)

    def eliminar_controller(self):
        id = self.id.get()
        resp = self.confirmacion_eliminar("eliminar")
        if resp:
            respuesta = coches.Coches.eliminar(id)
        else:
            respuesta = False
        self.respuesta_sql(respuesta)

    def consultar_controller(self, filas):
        registros = coches.Coches.consultar()
        if len(registros) > 0:
            num_coches = 1
            for fila in registros:
                 filas = filas + (f"Coche # {num_coches}\nID: {fila[0]}\nMarca: {fila[1]}\nColor: {fila[2]}\nModelo: {fila[3]}\nVelocidad: {fila[4]}\nPotencia: {fila[5]}\nAsientos: {fila[6]}")
                 num_coches += 1
        else:
            filas = ("\n\n\t NO existen datos que mostrar por el momento")
        return filas

    def modificar_controller(self):
        id = self.id.get()
        coche1=coches.Coches(self.marca.get(), self.color.get(), self.modelo.get(), self.velocidad.get(), self.potencia.get(), self.asientos.get())
        respuesta = coche1.actualizar(id)
        self.respuesta_sql(respuesta)

    def buscar_controller(self, tipo_accion):
        id =self.id.get()
        coche1 = coches.Coches.buscar(id)
        if len(coche1) > 0:
            messagebox.showinfo(title="... ¡Registro  encontrado! ...", message=f"...El registro fue encontrado con exito, puedes {tipo_accion}...")
            self.cambiar_estado_btn(True, tipo_accion)
        else:
            messagebox.showerror(title="... ¡Verifica por favor! ...", message=f"...El registro no fue encontrado, no es posible {tipo_accion}...")
            self.cambiar_estado_btn(False, tipo_accion)
        del coche1

    def main(self):
        self.borrarPantalla()
        Label(self.ventana, text = "\n...::: M E N U  P R I N C I P A L :::...").pack(pady=10)
        Button(self.ventana, text = "1.- Coches", command = self.menu_acciones).pack(pady=5)
        Button(self.ventana, text = "2.- Salir", command = self.ventana.quit).pack(pady=5)


if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()