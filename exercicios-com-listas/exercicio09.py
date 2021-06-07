#Faça um Programa que leia um vetor A com 10 números inteiros, 
# calcule e mostre a soma dos quadrados dos elementos do vetor. 

a = []

for numero in range(10):
    a.append(int(input("Digite um número inteiro: ")))


soma_dos_quadrados = 0

for numero in a:
    soma_dos_quadrados += numero ** 2

print(f"A soma dos quadrados dos números é: {soma_dos_quadrados}")