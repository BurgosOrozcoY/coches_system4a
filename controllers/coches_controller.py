from models import coches_model

class CochesController:
    #   CONTROLADOR del SISTEMA
    def insertar_controller(self):
        coche1=coches_model.CochesModel(self.marca.get(), self.color.get(), self.modelo.get(), self.velocidad.get(), self.potencia.get(), self.asientos.get())
        respuesta = coche1.insertar()
        self.respuesta_sql(respuesta)

    def eliminar_controller(self):
        id = self.id.get()
        resp = self.confirmacion_eliminar("eliminar")
        if resp:
            respuesta = coches_model.CochesModel.eliminar(id)
        else:
            respuesta = False
        self.respuesta_sql(respuesta)

    def consultar_controller(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in coches_model.CochesModel.consultar():
            self.tree.insert("", "end", values=row)

    def modificar_controller(self):
        id = self.id.get()
        coche1=coches_model.CochesModel(self.marca.get(), self.color.get(), self.modelo.get(), self.velocidad.get(), self.potencia.get(), self.asientos.get())
        respuesta = coche1.actualizar(id)
        self.respuesta_sql(respuesta)

    def buscar_controller(self, tipo_accion):
        id =self.id.get()
        coche1 = coches_model.CochesModel.buscar(id)
        if len(coche1) > 0:
            self.encontrado(coche1, tipo_accion)