acervo = [] #Declaração do array
op = 999

def cadastrarLivro(acervo):
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        while True:
            try:
                ano = int(input("Digite o ano do livro:"))
                break
            except ValueError:
                print("O ano precisa ser um número!")

        acervo.append({"titulo": titulo, "autor": autor, "ano": ano}) #Adiciona no array
        print(f"Livro cadastrado:")
        print(acervo) #mostra na tela

def procurarLivro(acervo):
        procurado = input("Digite o Livro que deseja procurar: ")
        encontrado = None

        for livro in acervo:
            if livro["titulo"] == procurado:
                encontrado = livro
                break

        if encontrado:
            print(f"Livro encontrado! {encontrado}")
        else:
            print(f"O livro {procurado} não está no nosso acervo =/")

def listarLivros(acervo):
        if len(acervo) == 0:
            print("Acervo vazio")
        else:
            for livro in acervo:
                livro.get("ano", "Ano indisponível")
                print(f"{livro["titulo"]} ({livro["ano"]}) - {livro["autor"]}")


while True: #Repetição da função até que o usuário escolha 0
    op = int(input("Bem vindo! \n1 - Cadastrar Livro\n2 - Procurar\n3 - Listar\n0 - Sair\n")) #Mostrar na tela as opções   

    if op == 1: #Pede os dados do livro para cadastrá-lo (adicionar no array)
        cadastrarLivro(acervo)
    
    elif op == 2: #Procurar livros a partir do nome
        procurarLivro(acervo)
        
    elif op == 3: #Listar todos os livros
        listarLivros(acervo)

    elif op == 0: #Sair do programa
        print("Ok, programa encerrando...")
        break
    else:
        print(f"Por favor, digite um número válido")
        break


#Pergunta 1: O int no input do livro
#Pergunta 2: O int no input do livro
#Pergunta 3: Apenas na parte de cadastrar o livro e listar ele