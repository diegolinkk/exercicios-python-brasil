# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = float(input("Digite um terceiro número: "))

a = (n1 * 2) + (n2 / 2)
b = (n1 * 3) + n3
c = n3 ** 3

print("O produto do dobro do primeiro com metade do segundo: {}".format(a))
print("A soma do triplo do primeiro com o terceiro: {}".format(b))
print("O terceiro elevado ao cubo: {}".format(a))