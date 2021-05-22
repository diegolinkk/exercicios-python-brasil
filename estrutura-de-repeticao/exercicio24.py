#Faça um programa que calcule o mostre a média aritmética de N notas.

continuar = 's'
media = 0
soma = 0
numero_de_elementos = 0

while continuar.lower() == 's':
    numero = int(input("Digite um número: "))
    soma += numero
    numero_de_elementos +=1

    continuar = input("Continuar? [s/n]: ")

if numero_de_elementos >=1:
    media = soma / numero_de_elementos

print(f"A média dos números é: {media:.2f}")