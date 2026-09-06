matriz = [[1, 2, 3], [4, 5, 6]]

matriz.append([7, 8, 9])
print(matriz[1][2])

for linha in matriz:
    for valor in linha:
        print(valor, end=" ")
    print()


matriz2 = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Valor [{i + 1}][{j + 1}]: "))
        linha.append(valor)
    matriz2.append(linha)


for linha in matriz2:
    for valor in linha:
        print(valor, end=" ")
    print()