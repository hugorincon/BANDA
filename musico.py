from instrumento import instrumento
from guitarra import guitarra
from bajo import bajo
from tiple import tiple

class musico():
    def tocar(self):
        self.instrumento.tocar()

    def asignar_instrumento(self, instrumento):
        self.instrumento = instrumento