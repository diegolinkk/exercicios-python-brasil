#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
#  Não utilize a função de potência da linguagem. 

base =int(input("DIgite a base: "))
expoente = int(input("Digite o expoente"))

potencia = base


for n in range(expoente -1):
    potencia *= base

print(potencia)