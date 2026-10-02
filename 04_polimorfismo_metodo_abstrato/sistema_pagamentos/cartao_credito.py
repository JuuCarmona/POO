from pagamento import Pagamentos

class Cartao_credito(Pagamentos):
    def __init__(self,valor,numero_cartao):
        super().__init__(valor)
        self.numero_cartao = numero_cartao

    def processarpagamento(self):
        taxa = self.valor * 0.10
        total = self.valor + taxa
        return total
    
    def exibir_pagamento(self):
        print('PAGAMENTO CARTÃO DE CRÉDITO')
        print(f'Valor original:R${self.valor}')
        print(f'Número do cartão:{self.numero_cartao}')
        print(f'Valor com taxa: R${self.processarpagamento()}')
        print('-'*30)
