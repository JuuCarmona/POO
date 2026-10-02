from abc import ABC, abstractmethod

class Forma(ABC):
    def __init__(self,cor):
        self.cor = cor

    @abstractmethod
    def calcular_area(self):
        pass
