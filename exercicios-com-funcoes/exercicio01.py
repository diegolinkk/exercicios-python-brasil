# Faça um programa para imprimir:
#     1
#     2   2
#     3   3   3
#     .....
#     n   n   n   n   n   n  ... n

def contador(n):
    for numero in range(1,n):
        string = str(numero) + " "
        string *= numero
        print(string)


contador(15)