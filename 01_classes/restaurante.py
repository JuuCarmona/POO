class Restaurante:
    def __init__(self,nome,categoria,ativo=False,avaliacao=0,tempo_entrega=0):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.avaliacao = avaliacao
        self.tempo_entrega = tempo_entrega

    def __str__(self):
        return f'{self.nome}|{self.categoria}'
    
restaurante_formatado = Restaurante(nome='Bom Sabor', categoria='tradicional')
print(restaurante_formatado)
