from abc import ABC,abstractmethod

class Funcionario(ABC):
    def __init__(self,nome,salarioBase):
        self.nome = nome
        self.salario_base = salarioBase
    
    @abstractmethod

    def calcularSalario(self):
        pass

    def exibir_salario(self):
        print(f'o nome do funcionario:{self.nome}, e seu salário:{self.salario_base}')
