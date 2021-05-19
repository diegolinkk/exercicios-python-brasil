#Altere o programa anterior para mostrar no final a soma dos números

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))

soma = 0

for n in range(n1+1,n2):
    print(n)
    soma += n


print("A soma dos intervalos é de : {}".format(soma))