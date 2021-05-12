#Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

primeiro = n1
segundo = n2
terceiro = n3

if terceiro > segundo:
    terceiro, segundo = segundo, terceiro

if segundo > primeiro:
    segundo,primeiro = primeiro,segundo

if terceiro > segundo:
    terceiro,segundo = segundo,terceiro

print(f"Primeiro: {primeiro}")
print(f"Segundo: {segundo}")
print(f"Terceiro: {terceiro}")