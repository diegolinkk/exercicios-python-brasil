# Utilize uma lista para resolver o problema a seguir. 
# Uma empresa paga seus vendedores com base em comissões. 
# O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
# Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. 
# Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante
#Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

faixa_de_salarios = [
    ["R$200 - R$299",0],
    ["R$300 - R$399",0],
    ["R$400 - R$499",0],
    ["R$500 - R$599",0],
    ["R$600 - R$699",0],
    ["R$700 - R$799",0],
    ["R$800 - R$899",0],
    ["R$900 - R$999",0],
    ["R$1000 em diante",0]
]


while True:
    vendas = float(input("Digite o valor das vendas: R$"))

    if vendas <= 0:
        break

    salario = 200.00 + vendas * 0.09

    #fórmula para chegar a posição sem ifs aninhados
    posicao = (salario // 100) - 2 #por exemplo, se for 304 que da divisão inteira 3 e subtrai 2 pra cair na posição 1 (300 a 399) 
    
    if posicao > len(faixa_de_salarios) -1 :  #se for acima de 1k, precisa direcionar para não ultrapassar o index
        faixa_de_salarios[-1][1] += 1 
    else:
        faixa_de_salarios[int(posicao)] [1] +=1

for faixa_salarial, quantidade in faixa_de_salarios:
    print(f"Faixa de salário: {faixa_salarial} - Quantidade - {quantidade}")
