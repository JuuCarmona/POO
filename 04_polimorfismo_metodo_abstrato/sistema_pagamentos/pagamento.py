from abc import ABC,abstractmethod

class Pagamentos(ABC):
    def __init__(self,valor):
        self.valor = valor

    @abstractmethod
    def processarpagamento(self):
        pass

    def exibir_pagamento(self):
        print(f'valor original: R$:{self.valor}')
        print (f'valor final: R$:{self.processarpagamento()}')
