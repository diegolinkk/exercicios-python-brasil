#Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. 
# Um número primo é aquele que é divisível apenas por um e por ele mesmo. 
# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

numero = int(input("Digite um número: "))
divisor = numero
contador_divisoes = 0

while divisor >=1:
    if numero % divisor == 0:
        contador_divisoes +=1
    
    divisor -=1

if contador_divisoes <=2:
    print("O número é primo")
else:
    print("O número não é primo")