from veiculo import Veiculo

class Carros(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def __str__(self):
        return f'{super().__str__()}, portas: {self.portas}'
