# Faça um programa que mostre os n termos da Série a seguir:

#       S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
# Imprima no final a soma da série. 

a = 2
b = 3

s = 1

print(f"S = 1/1 +",end=" ")

for i in range(6):
    s += a / b
    print(f"{a}/{b} +",end=" ")
    a +=1
    b +=2

print(f"S = {s}")