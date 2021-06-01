# Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos. 


a = 1
b = 2
h = 1

n = int(input("Digite quantos termos: "))

print(f"H =",end = " ")

for _ in range (n - 1):
    h += a / b
    print(f"+ {a}/{b}",end=" ")
    b += 1

print(f"= {h}")