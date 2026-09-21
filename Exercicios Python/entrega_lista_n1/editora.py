class Editora:
    def __init__(self, nome, cidade, fundacao):
        self.nome = nome
        self.cidade = cidade
        self.fundacao = fundacao

    @property
    def fundacao(self):
        return self._fundacao

    @fundacao.setter
    def fundacao(self, valor):
        if valor < 1500:
            raise ValueError("O ano de fundacao nao pode ser menor que 1500")
        if valor > 2026:
            raise ValueError("O ano de fundacao nao pode ser maior que 2026")
        self._fundacao = valor

    def idade(self):
        return 2026 - self.fundacao

    def __str__(self):
        return f"{self.nome} - {self.cidade} ({self.fundacao})"


editora = Editora("Companhia das Letras", "Sao Paulo", 1986)

if __name__ == "__main__":
    print(editora)
    print(f"Idade em 2026: {editora.idade()} anos")
