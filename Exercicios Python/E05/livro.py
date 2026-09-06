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


livro = Livro("O nome do vento", "Patrick Rothfuss", 2009)
# print(livro.descricao())
# print(livro.idade())

acervo = [
    Livro("O nome do vento", "Patrick Rothfuss", 2009),
    Livro("O temor do Sabio", "Patrick Rothfuss", 2014),
    Livro("The Witcher A espada do destino", "Andrzej Sapkowski", 1992),
    Livro("The Witcher O Sangue dos Elfos", "Andrzej Sapkowski", 1993)
]

user = Usuario("Daniel", "2505002")
emp = Emprestimo(livro, user, "02/09/2026")

if __name__ == "__main__":
    acervo = [
        Livro("O nome do vento", "Patrick Rothfuss", 2009),
        Livro("O temor do Sabio", "Patrick Rothfuss", 2014)
    ]


    livroNovo = Livro("The Witcher O Último Desejo", "Andrzej Sapkowski", 1993)
    print(livroNovo)
    

    newUser = Usuario("Eric", "390924")
    newEmp = Emprestimo(livroNovo, newUser, "02/09/2026")
    print(newEmp)

    print(newEmp.livro.titulo)

    newEmp.devolver()
    print(newEmp)
    

    newUser2 = Usuario("Menechelli", "555555")
    newUser2.limite = 4
    newEmp2 = Emprestimo(livroNovo, newUser2, "02/09/2026")
    print(newEmp2)