class Revista:
    def __init__(self, titulo, edicao, ano):
        self.titulo = titulo
        self.edicao = edicao
        self.ano = ano

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        if not valor.strip():
            raise ValueError("titulo vazio")
        self._titulo = valor

    @property
    def edicao(self):
        return self._edicao

    @edicao.setter
    def edicao(self, valor):
        if valor <= 0:
            raise ValueError("edicao tem de ser maior que zero")
        self._edicao = valor

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, valor):
        if valor < 1450 or valor > 2026:
            raise ValueError("ano fora de 1450..2026")
        self._ano = valor

    def __str__(self):
        return f"{self.titulo} - n. {self.edicao} ({self.ano})"
