from abc import ABC, abstractclassmethod

class instrumento(ABC):
    @abstractclassmethod
    def tocar(self):
        pass
    @abstractclassmethod
    def afinar(self):
        pass