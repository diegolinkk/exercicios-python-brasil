#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

quantidade  = int(input("Digite a quantidade de números você quer na sequência Fibonacci: "))

a = 1
b = 1

print(a)
print(b)

for _ in range(quantidade):
    a,b = b, (a+b)
    print(b)