def cadastrar():
    try:
        ano = int(campo_ano.get())
        livro = Livro(campo_titulo.get(), campo_autor.get(), ano)
        acervo.append(livro)
    except ValueError as erro:
        resultado.config(text=str(erro), fg="red")
