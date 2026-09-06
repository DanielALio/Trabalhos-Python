class Pessoa:
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura

    def imc(self):
        return (self.peso / (self.altura * self.altura))

pedro = Pessoa("Pedro", 96, 1.87)
print(pedro.nome, "-", pedro.peso)
print(pedro.imc())
