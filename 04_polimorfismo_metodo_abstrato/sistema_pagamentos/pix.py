rom pagamento import Pagamentos

class Pix(Pagamentos):
    def __init__(self,valor,chave):
        super().__init__(valor)
        self.chave = chave

    def processarpagamento(self):
        return self.valor
    
    def exibir_pagamento(self):
        print('PAGAMENTO PIX')
        print(f'valor original:R${self.valor}')
        print(f'chave pix:{self.chave}')
        print('-'* 30)
