class Pessoa:
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura

    def imc(self):
        return (self.peso / (self.altura * self.altura))

daniel = Pessoa("Daniel", 70, 1.70)
print(daniel.nome, "-", daniel.peso)
print(daniel.imc())
