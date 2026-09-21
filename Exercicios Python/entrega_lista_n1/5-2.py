class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def descricao(self):
        print(f"{self.titulo} - {self.autor}")
