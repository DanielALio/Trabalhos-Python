def cadastrar(acervo, titulo, autor, ano):
    livro = {"titulo": titulo, "autor": autor, "ano": ano}
    acervo.append(livro)

def buscar(acervo, titulo):
    for livro in acervo:
        if livro["titulo"] == titulo:
            return livro
        return None

if __name__ == "__main__":
    teste = []
    cadastrar(teste, "daniel", "daniel", 2505)
    print(buscar(teste, "daniel"))