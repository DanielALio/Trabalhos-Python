from dominio.livro import Livro
from dominio.usuario import Usuario
from dominio.emprestimo import Emprestimo
from datetime import date

acervo = []
emprestimo = []
usuario = Usuario("Aluno", 9999)

while True:
    print("===BIBLIOTECA===")
    print("1 - CADASTRAR LIVRO")
    print("2 - LISTAR ACERVO")
    print("3 - EMPRÉSTIMO")
    print("4 - DEVOLVER")
    print("0 - SAIR")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano = int(input("Digite o ano que o livro foi escrito: "))

        try:
            acervo.append(Livro(titulo, autor, ano))
            print(f"Livro cadastrado: {titulo}, {autor} - {ano}")
        except ValueError as erro:
            print(f"Erro: {erro}")

    elif opcao == 2:
        if not acervo:
            print("Acervo vazio, cadastre um livro primeiro!")
        else:
            for livro in acervo:
                print(f"- {livro}")

    elif opcao == 0:
        print("Até logo...")
        break

    elif opcao == 3:
        procurado = input("Titulo do livro que deseja emprestar: ")
        escolhido = None

        for livro in acervo:
            if livro.titulo == procurado:
                escolhido = livro

        if escolhido is None:
            print("Livro não está no acervo!!!")
        else:
            emprestimo.append(Emprestimo(escolhido, usuario, "02/09/2026"))
            print(f"Empréstimo realizado: {emprestimo[-1]}")

    elif opcao == 4:
        procurado = input("Titulo do livro que deseja devolver: ")
        escolhido = None

        for emp in emprestimo:
            if emp.livro.titulo == procurado:
                escolhido = emp

            try:
                emp.devolver()
                print(f"Livro {livro} devolvido!")
            except ValueError as erro:
                print(f"Não foi possível devolver: {erro}")

        #Perguntar para o Eric depois como faz isso
        
            