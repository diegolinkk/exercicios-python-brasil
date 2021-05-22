#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

repetir = 's'
soma = 0

# primeira vez
numero = int(input("Digite um número: "))
maior = numero
menor = numero
soma += numero
repetir = input("Continuar ? [s/n]: ")

while repetir.lower() != 'n':
    numero = int(input("Digite um número: "))

    soma += numero
    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

    repetir = input("Continuar ? [s/n]: ")

print(f"O maior número digitado foi: {maior}")
print(f"O menor número digitado foi: {menor}")
print(f"A soma dos números digitado foi: {soma}")