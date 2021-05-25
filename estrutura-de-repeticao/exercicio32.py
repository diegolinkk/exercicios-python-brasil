# #Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120

numero = int(input("Fatorial de: "))
fatorial = numero
contador = numero -1

print(f"{numero}! = ", end=' . ')

while contador > 1:
    print(f"{contador}", end = ' . ')
    fatorial *= contador
    contador -= 1

print(f"{contador} = {fatorial}")