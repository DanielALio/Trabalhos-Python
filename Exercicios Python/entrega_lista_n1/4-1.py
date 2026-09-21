class Aluno:
    def __init__(self, nome):
        self.nome = nome


turma = []

for nome in ["Ana", "Bruno", "Carla"]:
    aluno = Aluno(nome)
    turma.append(aluno)

for aluno in turma:
    print(aluno.nome)
