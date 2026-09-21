from revista import Revista


revista_valida = Revista("Superinteressante", 450, 2024)
print(revista_valida)

casos_invalidos = [
    ("", 450, 2024),
    ("Piaui", 0, 2024),
    ("Piaui", 200, 3000),
]

for titulo, edicao, ano in casos_invalidos:
    try:
        Revista(titulo, edicao, ano)
    except ValueError as erro:
        print(erro)

try:
    revista_valida.edicao = 0
except ValueError as erro:
    print(erro)

try:
    revista_valida.titulo = ""
except ValueError as erro:
    print(erro)

print(revista_valida)
