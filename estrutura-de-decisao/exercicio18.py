#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input("Digite o dia [dd]: "))
mes = int(input("Digite o mês [mm]: "))
ano = int(input("Digite o ano [aaaa]: "))

meses_com_trinta_dias = [2,4,6,9,11]

#data começa como True e vai passando por validações
data_valida = True

#validações - qualquer condição destas invalida a data
if dia > 31:
    data_valida = False

if mes > 12:
    data_valida = False

if dia < 1 or mes < 1:
    data_valida = False

if dia >30 and mes in meses_com_trinta_dias:
    data_valida = False

if ano < 0:
    data_valida = False



if data_valida:
    print(f"A data {dia}/{mes}/{ano} é válida")
else:
    print(f"A data {dia}/{mes}/{ano} NÃO é válida")