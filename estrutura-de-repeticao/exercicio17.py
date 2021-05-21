#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

numero = int(input("Digite um número: "))
numero_inicial = numero
fatorial = numero

while numero > 1:
    numero -=1
    fatorial *= numero

print(f"Fatorial de {numero_inicial} é: {fatorial}")