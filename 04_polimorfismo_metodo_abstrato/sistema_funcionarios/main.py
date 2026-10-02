from funcionario import Funcionario
from gerente import Gerente
from programador import Programador

funcionarios = [
    Gerente('Carlos',5000,1000),
    Programador('ana',4000,10,50)
]

for i in funcionarios:
    print(i.nome, "recebe")
    i.exibir_salario()
