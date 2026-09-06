#Exercicio 3

matriz = []

for linha in range(3):
    linha = []
    for valor in range(3): #for(int i = 0; i<3; i++)
        valor = float(input("Digite um valor: "))
        linha.append(valor)
    matriz.append(linha)

print(f"A soma da linha 1: {sum(matriz[0])}")
print(f"A soma da linha 2: {sum(matriz[1])}")
print(f"A soma da linha 3: {sum(matriz[2])}")

print(f"A soma da matriz é {sum(matriz[0]) + sum(matriz[1]) + sum(matriz[2])}")