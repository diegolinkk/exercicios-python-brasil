#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

numero = int(input("Digite um número: "))
divisor = numero
contador_divisoes_inteiras= 0
divisores = []

while divisor >=1:
    if numero % divisor == 0:
        contador_divisoes_inteiras +=1
        divisores.append(divisor)
    divisor -=1

if contador_divisoes_inteiras <=2:
    print("O número é primo")
else:
    print("O número não é primo")
    for n in divisores:
        print(f"O número é divisível por: {n}")
