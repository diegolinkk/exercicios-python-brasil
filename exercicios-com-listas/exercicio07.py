#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números. 

numeros = []

for _ in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)


print(f"Soma dos números: {sum(numeros)}")

multiplicacao = 1

for numero in numeros:
    multiplicacao *= numero

print(f"Multiplicação dos números: {multiplicacao}")
print(f"Números: {numeros}")