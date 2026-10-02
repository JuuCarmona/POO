from livro import Livro
livro_biblioteca = Livro('2012','Brian DAmato','2012')
print(f' Antes de emprestar (biblioteca): Livro disponível?{livro_biblioteca.disponivel}')

livro_biblioteca.emprestar()
print(f'Depois de emprestar(biblioteca): Livro disponivel?{livro_biblioteca.disponivel}')

ano_especifico = 2012
livros_disponiveis_ano = Livro.verificar_disponibilidade(2012)
print(livros_disponiveis_ano)
