#Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

numero = int(input("Digite até que número você quer encontrar os números primos: "))

for i in range (1,numero + 1):
    divisor = i
    contador_divisoes = 0

    #percorre o número para fazer as divisões
    while divisor >=1:
        #valida as divisões inteiras
        if i % divisor == 0:
            contador_divisoes +=1
        
        divisor -=1
    
    #imprime somente se o número é primo
    if contador_divisoes <= 2:
        print(i)