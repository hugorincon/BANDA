from instrumento import instrumento
from guitarra import guitarra
from bajo import bajo
from tiple import tiple


class afinador():
    def __init__(self, musico):
        self.musico = musico
        self.instrumento = musico.instrumento
        
    def tocar(self):
        self.instrumento.afinar()