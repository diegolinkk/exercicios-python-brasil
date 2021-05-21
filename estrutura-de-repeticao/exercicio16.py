#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

a = 1
b = 1

print(a)
print(b)

while True:
    a,b = b, (a + b)

    if b > 500:
        break
    
    print(b)