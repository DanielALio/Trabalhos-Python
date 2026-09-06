acervo = [
    {"titulo": "Cartas de um Diabo ao seu Aprendiz", "autor": "C.S Lewis", "ano": 1947},
    {"titulo": "Alice no país das Maravilhas", "autor": "Lewis Carrol", "ano": 1900},
    {"titulo": "O Livro de Ouro das Copas", "autor": "Lycio Ribas", "ano": 2026}
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


acervo.append({"titulo": "Biblia Sagrada", "autor": "Jeová"})

for livro in acervo:
    ano = livro.get("ano", "ano desconhecido")
    print(f"{livro["titulo"]} ({ano})")