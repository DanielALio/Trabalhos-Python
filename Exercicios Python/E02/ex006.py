#Exercício 1

a = []

for valor in range(5):
    valor = int(input("Digite um valor inteiro: "))
    a.append(valor)

print(f"A soma entre esses valores é {sum(a)}")
print(f"A média entre esses valores é {sum(a)/len(a)}")

