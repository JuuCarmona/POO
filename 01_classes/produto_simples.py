class ProdutoSimples:
    def __init__(self,nome,preco,quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        total = self.preco * self.quantidade
        print(f"O valor total do produto {self.nome} em estoque é {total}")

p1 = ProdutoSimples("Kitkat",5,20)
p2 = ProdutoSimples("CocaCola",8,25)

p1.calcular_total()
p2.calcular_total()
