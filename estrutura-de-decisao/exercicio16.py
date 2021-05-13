# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
# O programa deverá pedir os valores de a, b e c e fazer as consistências, 
# informando ao usuário nas seguintes situações:

#     Se o usuário informar o valor de A igual a zero, 
# a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;

#     Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#     Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#     Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário; 

from math import sqrt


a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = ( b ** 2) - 4 * a * c
abs

x1 = ((b * -1) + sqrt(abs(delta))) / (a * 2)

x2 = ((b * -1) - sqrt(abs(delta))) / (a * 2)



if a == 0:
    print("A equação não é de segundo grau.")
elif delta < 0:
    print("A equação não possui raízes reais")
elif delta == 0:
    print(f"Delta é zero. Única raiz real: {x1}")
else:
    print(f"x1 = {x1}\n x2 = {x2}")

