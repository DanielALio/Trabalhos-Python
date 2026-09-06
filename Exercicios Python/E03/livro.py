livro = {
    "titulo": "O nome do Vento",
    "ano": 2009,
    "autor": "Patrick Rothfuss"

}
print(livro["autor"])
print(livro)

for chave, valor in livro.items():
    print(f"{chave}: {valor}")

if "ano" in livro:
    print(f"O livro tem ano, e é {livro['ano']}")


if "paginas" not in livro:
    print(f"Não é possível acessar o número de páginas")