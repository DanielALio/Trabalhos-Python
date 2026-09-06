notas = []

notas.append(5) #Adiciona valores no final da array

print(notas)
print("Quantas: ", len(notas)) #Tamanho do array
print("Primeira: ", notas[0]) 
print("Última: ", notas[-1]) #-1 é a ultima, independente do tamanho
print("Soma: ",  sum(notas)) #Soma das notas
print("Média: ", sum(notas)/len(notas)) 
print("Maior: ", max(notas)) #Maior número do array

for nota in notas:
    print(nota)