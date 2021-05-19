#Faça um programa que leia 5 números e informe o maior número. 



comparador = 1

maior = int(input("Digite um número: "))

while comparador <=4:
    numero = int(input("Digite outro número: "))
    if numero > maior:
        maior = numero
    comparador +=1

print("O maior número é: {}".format(maior))
