# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
#F =  (C × 9/5) + 32

c = float(input("Digite a temperatura em graus Celcius: "))
f = (c * (9/5)) + 32
print("A temperatura em graus Celcius é: {:.2f}".format(f))