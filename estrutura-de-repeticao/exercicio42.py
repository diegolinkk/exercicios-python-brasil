#Faça um programa que leia uma quantidade indeterminada de números positivos 
# e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. 
# A entrada de dados deverá terminar quando for lido um número negativo.

numeros_entre_0_25 = 0
numeros_entre_26_50 = 0
numeros_entre_51_75 = 0
numeros_entre_76_100 = 0

while True:
    numero = int(input("Digite um número inteiro ou um número negativo para sair: "))
    if numero < 0:
        break

    if numero in range(0,26):
        numeros_entre_0_25 +=1
    elif numero in range(26,51):
        numeros_entre_26_50 +=1
    elif numero in range(51,76):
        numeros_entre_51_75 +=1
    elif numero in range(76,101):
        numeros_entre_76_100 +=1

print(f"Números entre 0 e 25:  {numeros_entre_0_25}")
print(f"Números entre 26 e 50:  {numeros_entre_26_50}")
print(f"Números entre 51 e 75:  {numeros_entre_51_75}")
print(f"Números entre 76 e 100:  {numeros_entre_76_100}")