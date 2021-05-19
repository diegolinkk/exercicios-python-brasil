#Faça um programa que leia 5 números e informe a soma e a média dos números

soma = 0

for contador in range(5):
    numero = int(input("Digite um número: "))
    soma += numero

print(f"A soma dos números digitados é: {soma}")
print(f"A média dos números digitados é: {soma / 5}")
