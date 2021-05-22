#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.


repetir = 's'

numero = int(input("Digite um número entre 0 e 1000: "))
repetir = input("Repetir? [s/n]: ")

if numero >=0 and numero <=1000:
    soma, maior, menor = numero, numero, numero
else:
    soma = 0
    maior = 0
    menor = 0


while repetir.lower() != 'n' and numero >= 0 and numero <= 1000:
    numero = int(input("Digite outro número: "))
    if numero >=0 and numero <=1000:
        soma += numero
        maior = numero if numero > maior else maior
        menor = numero if numero < menor else menor
    repetir = input("Repetir? [s/n]: ")

print(f"A soma dos números é : {soma}")
print(f"O maior número digitado é : {maior}")
print(f"O maior menor digitado é : {menor}")