#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

numero = int(input("Digite um número: "))
divisor = numero
contador_divisoes_inteiras = 0

while divisor >=1:
    if (numero % divisor) == 0:
        contador_divisoes_inteiras +=1
    divisor -=1

if contador_divisoes_inteiras <= 2:
    print("O número é primo")
else:
    print("O número não é primo")