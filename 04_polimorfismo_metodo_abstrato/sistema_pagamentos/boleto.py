from pagamento import Pagamentos

class Boleto(Pagamentos):
    def __init__(self,valor,nome_completo,cpf):
        super().__init__(valor)
        self.nome_completo = nome_completo
        self.cpf = cpf

    def processarpagamento(self):
        return self.valor + 3.0
    
    def exibir_pagamento(self):
        print('PAGAMENTO BOLETO')
        print(f'Valor original:R${self.valor}')
        print(f'Gerando boleto para {self.nome_completo}')
        print(f'CPF:{self.cpf}')
        print(f'Valor final:R${self.processarpagamento()}')
        print('-' *30)
