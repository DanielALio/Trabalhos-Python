from acervo import cadastrar, buscar

livros = []

titulo = "O Temor do Sabio"
autor = "Patrick Rothfuss"
ano = 2011
cadastrar(livros, titulo, autor, ano)

achado = buscar(livros, titulo)

if achado:
    print(f"{achado} Encontrado!")
else:
    print(f"{achado} não encontrado =<")