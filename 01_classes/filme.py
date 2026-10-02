class Filme:
    def __init__(self,nome,duracao,classificacao,genero):
        self.nome = nome
        self.duracao = duracao
        self.classificacao = classificacao
        self.genero = genero

    def exibir_info(self):
        print(f"O filme {self.nome}, tem duração de {self.duracao} minutos, sua classifição é de {self.classificacao} anos , e o genero é {self.genero}")

filme1 = Filme("IT",120,"18","terror")
filme1.exibir_info()
