acervo = [
    {"titulo": "Tempo do Despreso", "autor": "Andrzej Sapkowski", "ano": 1995},
    {"titulo": "Batismo de fogo", "autor": "Andrzej Sapkowski", "ano": 1996},
    {"titulo": "Torre da Andorinha", "autor": "Andrzej Sapkowski", "ano": 1997}
]

print(f"O acervo tem {len(acervo)} livro(s)")

for livro in acervo:
    print(f"{livro["titulo"]} ({livro["ano"]}) - {livro["autor"]}")

procurado = input("Título: ")
encontrado = None

for livro in acervo:
    if livro["titulo"] == procurado:
        encontrado = livro
        break


if encontrado:
    print(f"Livro encontrado! {encontrado}")
else:
    print(f"O livro {procurado} não foi encontrado no acervo =(")


acervo.append({"titulo": "A senhora do lago", "autor": "Andrzej Sapkowski"})

for livro in acervo:
    ano = livro.get("ano", "ano desconhecido")
    print(f"{livro["titulo"]} ({ano})")