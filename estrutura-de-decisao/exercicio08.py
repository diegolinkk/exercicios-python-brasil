#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

p1 = int(input("Digite o valor do primeiro produto: "))
p2 = int(input("Digite o valor do segundo produto: "))
p3 = int(input("Digite o valor do terceiro produto: "))

primeiro = p1
segundo = p2
terceiro = p3

if terceiro > segundo:
    terceiro,segundo = segundo,terceiro

if segundo > primeiro:
    segundo, primeiro = primeiro,segundo

if  terceiro > segundo:
    terceiro, segundo = segundo, terceiro

print("O produto que você deve comprar é o de valor: {}".format(terceiro))