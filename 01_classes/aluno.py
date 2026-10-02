class Aluno:
    def __init__(self,nome,nota1,nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular(self):
        media = (self.nota1 + self.nota2)/2
        if media >= 7:
            print("O aluno ,{self.nome},foi aprovado")
        else:
            print("O aluno ,{self.nome},não foi aprovado")

aluno1 = Aluno("Julia",7,9)
aluno2 = Aluno("Ana",2,7)

aluno1.calcular()
aluno2.calcular()
