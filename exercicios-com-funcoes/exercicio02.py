# Faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.


def imprimir(n):
    for numero in range(1, n+1):
        n = 1 #inicia no 1
        while n <= numero: #imprimi o caractere e adiciona 1, imprimi de novo e o faz até chegar no n´mero atual
            print(n,end=" ")
            n +=1

        print("") #pula uma linha

imprimir(5)