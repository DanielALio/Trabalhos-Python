def media(notas):
    return sum(notas)/len(notas)

def situacao(notas, corte=7.0):
    if notas >= corte:
        return "Aprovado"
    return "Reprovado"

def min_max(notas):
    return max(notas), min(notas)

notas = [7, 9, 5]
print(f"Média das notas: {media(notas)}")
print(f"Situação de uma nota 8: {situacao(8)}")
print(f"Situação de uma nota 8 com média 9: {situacao(8, 9.0)}")
menor, maior = min_max(notas)
print(f"A menor nota: {menor}. A maior nota: {maior}")