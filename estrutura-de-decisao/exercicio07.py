#Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

primeiro = n1
segundo = n2
terceiro = n3

if terceiro > segundo:
    terceiro,segundo = segundo,terceiro

if segundo > primeiro:
    segundo,primeiro = primeiro,segundo

if terceiro > segundo:
    terceiro,segundo = segundo,terceiro

print(f"O maior dos números é: {primeiro}")
print(f"O menor dos números é: {terceiro}")