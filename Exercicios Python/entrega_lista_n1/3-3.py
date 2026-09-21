class EditoraValidacaoNoInit:
    def __init__(self, nome, cidade, fundacao):
        if fundacao < 1500:
            raise ValueError("O ano de fundacao nao pode ser menor que 1500")
        if fundacao > 2026:
            raise ValueError("O ano de fundacao nao pode ser maior que 2026")

        self.nome = nome
        self.cidade = cidade
        self.fundacao = fundacao


class EditoraValidacaoNoSetter:
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
