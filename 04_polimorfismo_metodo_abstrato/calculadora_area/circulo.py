from forma import Forma

class Circulo(Forma):
    def __init__(self,cor,raio):
        super().__init__(cor)
        self.raio = raio

    def calcular_area(self):
        area = (self.raio **2)
        print("A área do circulo é igual a:", area)
