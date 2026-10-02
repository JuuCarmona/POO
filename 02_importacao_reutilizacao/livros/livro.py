class Livro:
    livros = []

    def __init__(self,titulo,autor,ano_publicado):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicado = ano_publicado
        self.disponivel = True

    def __str__(self):
        return f'Livro:{self.titulo}|{self.autor}|{self.ano_publicado}'

    def emprestar(self):
        self.disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicado == ano and livro.disponivel]
        return livros_disponiveis

livro1 = Livro('Romeu e Julieta','William Shakespeare',1591)
livro2 = Livro('Alice no país das maravilhas','Lewis Carroll',1865)
print(livro1)
print(livro2)

livro3 = Livro('Cinderela','Charles Perrault',1697)
print(livro3)
livro3.emprestar()
print(livro3.disponivel)

Livro.livros = [livro1,livro2,livro3]
