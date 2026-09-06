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
    cadastrar(teste, "pedro", "pedro", 2193)
    print(buscar(teste, "pedro"))