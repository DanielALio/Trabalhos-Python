class Usuario:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = int(id)
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
