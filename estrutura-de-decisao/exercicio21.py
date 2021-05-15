# Faça um Programa para um caixa eletrônico. 
# O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

saque = int(input("Digite o valor a ser sacado: "))

notas_de_100 = ""
notas_de_50 = ""
notas_de_10 = ""
notas_de_5 = ""
notas_de_1 = ""

if saque < 10 or saque > 600:
    print("Saque não permitido")
else:
    if saque >= 100:
        notas_de_100 = str(saque // 100) + " notas de 100,"
        saque = saque % 100
    if saque >= 50:
        notas_de_50 = str(saque // 50) + " notas de 50,"
        saque = saque % 50
    if saque >= 10:
        notas_de_10 = str(saque // 10) + " notas de 10,"
        saque = saque % 10
    if saque >=5:
        notas_de_5 = str(saque // 5) + " notas de 5,"
        saque = saque % 5
    notas_de_1 = str(saque) + " e notas de 1"

print(f"{notas_de_100} {notas_de_50} {notas_de_10} {notas_de_5} {notas_de_1}")
