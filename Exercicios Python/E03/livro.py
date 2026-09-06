livro = {
    "titulo": "Don casmurro",
    "ano": 1900,
    "autor": "Machado de Assis"

}
print(livro["autor"])
print(livro)

# livro["titulo"] = "Romeu e Julieta"
# livro["editora"] = "Thomas Nelson"
# print(livro)

for chave, valor in livro.items():
    print(f"{chave}: {valor}")

if "ano" in livro:
    print(f"O livro tem ano, e é {livro['ano']}")


if "paginas" not in livro:
    print(f"Não é possível acessar o número de páginas")