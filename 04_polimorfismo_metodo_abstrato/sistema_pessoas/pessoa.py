from abc import ABC,abstractmethod

class Pessoa(ABC):
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade

    @abstractmethod
    def apresentar(self):
        pass
