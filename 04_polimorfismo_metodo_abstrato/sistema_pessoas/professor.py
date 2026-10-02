from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade,disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def apresentar(self):
        print(f"Sou {self.nome}, tenho {self.idade} e leciono {self.disciplina}")
