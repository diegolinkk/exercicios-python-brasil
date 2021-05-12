#Faça um Programa que leia três números e mostre o maior deles. 

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("DIgite o terceiro número: "))

primeiro = a
segundo = b
terceiro = c

if terceiro > segundo:
    terceiro,segundo = segundo,terceiro

if segundo > primeiro:
    segundo,primeiro = primeiro, segundo

if terceiro > segundo:
    terceiro,segundo = segundo,terceiro

print(f"O maior número é: {primeiro}")