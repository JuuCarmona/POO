from funcionario import Funcionario

class Programador(Funcionario):
    def __init__(self,nome,salario_base,hora_extra,valor_hora):
        super().__init__(nome,salario_base)
        self.hora_extra = hora_extra
        self.valor_hora = valor_hora

    def calcularSalario(self):
        return self.salario_base + (self.hora_extra * self.valor_hora)
        
    def exibir_salario(self):
        print(f'o salário somado com a hora extra e valor da hora,ficou no total de: R$:{self.calcularSalario()}')
