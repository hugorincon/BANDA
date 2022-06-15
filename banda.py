from instrumento import instrumento
from guitarra import guitarra
from bajo import bajo
from tiple import tiple
from afinador import afinador
from musico import musico
from bandola import bandola
from random import randint, choice


class banda():
    def __init__(self):
        self.musicos = []

    def crear_banda(self):
        for i in range(randint(1, 5)):
            self.musicos.append(musico())
        for i in self.musicos:
            i.asignar_instrumento(self.generar_instrumento())

    def afinar(self):
        for musico in self.musicos:
            a = afinador(musico)
            a.tocar()

    def tocar(self):
        for musico in self.musicos:
             musico.tocar()


    def generar_instrumento(self):
        instrumentos = [guitarra(), bajo(), tiple(), bandola()]
        return choice(instrumentos)