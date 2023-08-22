class Asiento:
    def __init__(self,color,precio,registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    def cambiarColor(self, color:str):
        if color =="rojo" or color =="blanco" or color =="amarillo" or color =="verde" or color =="negro":
            self.color = color

class Auto:
    cantidadCreados = 0

    def __init__(self, modelo:str,precio:int,asientos,marca,motor,registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    def cantidadAsientos(self):
        cantidad = len(self.asientos)
        return cantidad

    def verificarIntegridad(self):
        asientos = self.cantidadAsientos()
        for i in range(asientos-1):
            if self.asientos[i].registro!=self.asientos[i+1].registro or self.asientos[0].registro!=self.registro:
                print("Las piezas no son originales")
                return
        if self.motor.registro != self.registro:
            print("Las piezas no son originales")
        else:
            print("Auto original")



class Motor:
    def  __init__(self,numeroCilindros:int,tipo:str,registro:int):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro= registro
    def cambiarRegistro(self, registro:int):
        self.registro = registro

    def asignarTipo(self,tipo:str):
        if tipo=="electrico" or tipo=="gasolina":
            self.tipo = tipo



