from funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self,nome,salario_base,bonus_fixo):
        super().__init__(nome,salario_base)
        self.bonus_fixo = bonus_fixo

    def calcularSalario(self):
       return self.salario_base + self.bonus_fixo
       

    def exibir_salario(self):
        print(f'O salario já com o bonus é:R${self.calcularSalario()}')
