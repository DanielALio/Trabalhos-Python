from datetime import date
class Livro:
    def __init__(self, titulo, autor, ano):
        if not titulo:
            raise ValueError("Titulo é obrigatório!")

        if not autor:
            raise ValueError("Autor é obrigatório")

        if ano < 1900 or ano > date.today().year:
            raise ValueError("Ano inválido")
        
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, valor):
        if valor < 1900 or valor > date.today().year:
            raise ValueError(f"Ano inválido: {valor}")
        self._ano = valor
        
    def __str__(self):
        return self.descricao()

    def descricao(self):
        return(f"{self.titulo} - {self.autor} ({self.ano})")

    def idade(self):
        return date.today().year - self.ano

    def classico(self):
        if self.idade() > 100:
            return("É clássico")
        else:
            return("Não é clássico")
