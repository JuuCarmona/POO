from abc import ABC,abstractmethod

class Pessoa:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade

    @abstractmethod
    def apresentar(self):
        pass
