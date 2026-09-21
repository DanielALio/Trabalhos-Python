def cadastrar():
    titulo = campo_titulo.get()
    autor = campo_autor.get()
    ano = campo_ano.get()

    try:
        livro = Livro(titulo, autor, int(ano))
        acervo.append(livro)
        atualizar_lista()
        campo_titulo.delete(0, tk.END)
        campo_autor.delete(0, tk.END)
        campo_ano.delete(0, tk.END)
        resultado.config(
            text=f"Livro cadastrado: {titulo}/{autor}/{ano}",
            fg="blue",
        )
    except ValueError as erro:
        resultado.config(text=f"Erro: {str(erro)}", fg="red")
