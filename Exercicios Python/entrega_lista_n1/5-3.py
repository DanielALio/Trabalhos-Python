def cadastrar():
    titulo = campo_titulo.get()
    autor = campo_autor.get()
    ano = campo_ano.get()

    try:
        livro = Livro(titulo, autor, int(ano))
        acervo.append(livro)
    except ValueError as erro:
        resultado.config(text=str(erro), fg="red")
