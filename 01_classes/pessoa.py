class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    def exibir_dados(self):
        print(f"Nome:{self.nome},idade:{self.idade}")

p1 = Pessoa("Julia",21)
p2 = Pessoa("Carla",40)

p1.exibir_dados()
p2.exibir_dados()
