# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores. 

numeros = []
pares = []
impares = []

for _ in range(20):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Todos os números digitados: ")
for numero in numeros:
    print(numero)

print("numeros pares: ")
for par in pares:
    print(par)

print("Números impares: ")
for impar in impares:
    print(impar)