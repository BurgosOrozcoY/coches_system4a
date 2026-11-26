

class CochesBD:
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos):
        self._marca = marca
        self._color = color
        self._modelo = modelo
        self._velocidad = velocidad
        self._potencia = potencia
        self._asientos = asientos



#Getters + Setters

    def getMarca(self):
        return self._marca

    def setMarca(self, marca):
        self._marca = marca

    def getColor(self):
        return self._color

    def setColor(self, color):
        self._color = color

    def getModelo(self):
        return self._modelo

    def setModelo(self, modelo):
        self._modelo = modelo

    def getVelocidad(self):
        return self._velocidad

    def setVelocidad(self, velocidad):
        self._velocidad = velocidad

    def getPotencia(self):
        return self._potencia

    def setPotencia(self, potencia):
        self._potencia = potencia 

    def getAsientos(self):
        return self._asientos

    def setAsientos(self, asientos):
        self._asientos = asientos

    # def modCoche(self, coche):
    #     marca = coche.setMarca(input("Marca: "))
    #     color = coche.setColor(input("Color: "))
    #     modelo = coche.setModelo(input("Modelo: "))
    #     velocidad = coche.setVelocidad(int(input("Velocidad: ")))
    #     potencia = coche.setPotencia(int(input("Potencia: ")))
    #     asientos = coche.setAsientos(int(input("Asientos: ")))



        