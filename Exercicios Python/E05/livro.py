from datetime import date

class Livro:
    def __init__(self, titulo, autor, ano):
        if not titulo:
            raise ValueError("Titulo é obrigatório!")

        if not autor:
            raise ValueError("Autor é obrigatório")

        if ano < 1450 or ano > date.today().year:
            raise ValueError("Ano inválido")
        
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, valor):
        if valor < 1450 or valor > date.today().year:
            raise ValueError(f"Ano inválido: {valor}")
        self._ano = valor
        
    def __str__(self):
        return self.descricao()

    def descricao(self):
        return(f"{self.titulo} - {self.autor} ({self.ano})")

    def idade(self):
        return date.today().year - self.ano

    def classico(self):
        if livro.idade() > 100:
            return("É clássico")
        else:
            return("Não é clássico")

class Usuario:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
        self.limite = 3

        if not nome:
            raise ValueError("Nome é obrigatório")

        if not id:
            print("Id obrigatório")

    def __str__(self):
        return(f"{self.nome} - {self.id} - Limite: {self.limite}")

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, valor):
        if valor > 3:
            raise ValueError("Limite do usuário atingido!!")
        self._limite = valor
    

    def podePegar(self):
        if self.limite > 3:
            return False
        return True

class Emprestimo:
    def __init__(self, livro, usuario, data):
        self.livro = livro
        self.usuario = usuario
        self.data = data
        self.entregue = False

    def devolver(self):
        if self.entregue:
            raise ValueError(f"Livro: {self.livro} Já foi devolvido")
        self.entregue = True

    def __str__(self):
        estado = "Devolvido" if self.entregue else "Em aberto"
        return(f"{self.usuario} -> {self.livro} {estado}")


livro = Livro("Romeu e Julieta", "Shakespeare", 1591)
# print(livro.descricao())
# print(livro.idade())

acervo = [
    Livro("Romeu e Julieta", "Shakespeare", 1591),
    Livro("A Arte da Guerra", "Sun Tzu", 1450),
    Livro("Biblia Sagrada", "Jesus Cristo", 1450),
    Livro("It - A coisa", "Stephen King", 1980)
]

user = Usuario("Pedro", "170707")
emp = Emprestimo(livro, user, "21/08/2026")

# print(emp)
# print(emp.livro.autor)
# print(user.id)

# emp.devolver()
# print(emp)
# emp.devolver()

# for livro in acervo:
#     print(f"{livro.titulo} - {livro.autor} ({livro.ano})")

if __name__ == "__main__":
    acervo = [
        Livro("Romeu e Julieta", "Shakespeare", 1591),
        Livro("A Arte da Guerra", "Sun Tzu", 1450)
    ]

    # for livro in acervo:
    #     print(f"{livro}")

    #Livro("Teste", "alguem", 3000)

    livroNovo = Livro("Cristianismo Puro e Simples", "C. S. Lewis", 1946)
    print(livroNovo)
    #livroNovo.ano = 3000 #coloquei em comentário porque se não o resto não aparece

    newUser = Usuario("Eric", "390924")
    newEmp = Emprestimo(livroNovo, newUser, "20/09/2026")
    print(newEmp)

    print(newEmp.livro.titulo)

    newEmp.devolver()
    print(newEmp)
    #newEmp.devolver() #coloquei em comentário porque se não o resto não aparece

    newUser2 = Usuario("Menechelli", "98394")
    newUser2.limite = 4
    newEmp2 = Emprestimo(livroNovo, newUser2, "20/09/2026")
    print(newEmp2)