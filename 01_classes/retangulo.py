class Retangulo:
    def __init__(self,largura,altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        area = (self.largura * self.altura)
        print(f"A área do retângulo é:{area}")

    def calcular_perimetro(self):
        perimetro = 2 * (self.largura + self.altura)
        print(f"O perímetro do retângulo é :{perimetro}")

r1 = Retangulo(5,10)
r1.calcular_area()
r1.calcular_perimetro()
