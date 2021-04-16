#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho_hora = float(input("Digite o quanto voce ganha por hora: "))
horas_trabalhadas = int(input("Digite quantas horas você trabalha por mês: "))

print("Seu salário mensal é: {0:.2f}".format(ganho_hora *  horas_trabalhadas))