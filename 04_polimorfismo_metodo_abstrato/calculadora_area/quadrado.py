from forma import Forma

class Quadrado(Forma):
    def __init__(self,cor,base,altura):
        super().__init__(cor)
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        print("A área do quadrado é:", area)
