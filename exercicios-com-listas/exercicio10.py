#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
#  cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. 

lista_1 = []
lista_2 = []

for i in range(10):
    lista_1.append(int(input("Digite um número inteiro: ")))
    lista_2.append(int(input("Digite outro número inteiro: ")))

lista_3 = [] #lista mesclada

for indice in range(len(lista_1)):
    lista_3.append(lista_1[indice])
    lista_3.append(lista_2[indice])

print(lista_3)