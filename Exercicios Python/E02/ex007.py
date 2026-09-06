#Exercicio 2

notas = []
acima = []

for valor in range(6):
    valor = float(input("Digite sua nota: "))
    notas.append(valor)

print(f"A maior nota é {max(notas)} e a menor é {min(notas)}")
print(f"A média da turma é {sum(notas)/len(notas)}")

for pos in notas:
    if pos >= 7:
        acima.append(pos)

print(f"Tem {len(acima)} nota(s) acima da média")