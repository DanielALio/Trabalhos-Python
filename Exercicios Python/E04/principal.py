from acervo import cadastrar, buscar

livros = []

titulo = "A arte da guerra"
autor = "Sun Tzu"
ano = 1500
cadastrar(livros, titulo, autor, ano)

achado = buscar(livros, titulo)

if achado:
    print(f"{achado} Encontrado!")
else:
    print(f"{achado} não encontrado =<")