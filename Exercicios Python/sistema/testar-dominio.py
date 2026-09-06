from dominio.livro import Livro
from dominio.usuario import Usuario
from dominio.emprestimo import Emprestimo

print("---Testando o domínio, sem tela nenhuma---")

livro = Livro('a arte da guerra', 'Shun Tzu', 1501)
print(f"Livro criado: {livro}")

try:
    Livro("Titulo random", "alguem", 3000)
    print(f"FALHOU, o ano 3000 passou")
except ValueError as erro:
    print("Ok, o sistema barrou", erro)

pedro = Usuario("pedro", 999)
emp = Emprestimo(livro, pedro, "24/09/2026")

emp.devolver()
print(f"Depois de devolver: {emp}")

try:
    emp.devolver()
    print(f"FALHOU, erro passou: Devolveu 2 vezes")
except ValueError as erro:
    print(f"OK, barrou: {erro}")

print()

acervo = [
    livro, 
    Livro("Iracema", "José de Alencar", 1865),
]

print(f"Livros no acervo: {len(acervo)}")
print(f"O autor do primeiro livro: {acervo[0].autor}")

procurado = "Iracema"
escolhido = None
for item in acervo:
    if item.titulo == procurado:
        escolhido = item
print(f"Livro encontrado: {escolhido}")

emprestimo = [emp, Emprestimo(acervo[1], pedro, "24/09/2026")]
em_aberto = [e for e in emprestimo if not e.entregue]
print(f"Empréstimos: {len(emprestimo)} - Em aberto: {len(em_aberto)}")