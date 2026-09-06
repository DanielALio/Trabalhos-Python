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
