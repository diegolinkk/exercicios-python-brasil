#Faça um programa que receba dois números inteiros e gere os números inteiros que 
# estão no intervalo compreendido por eles. 

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))

for n in range((n1 +1),n2):
    print(n)