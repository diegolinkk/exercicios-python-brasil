#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os. 
numeros = []

for _ in range(5):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

for numero in numeros:
    print(numero)