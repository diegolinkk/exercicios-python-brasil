# #Faça um Programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e 
# que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#     Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#     comprar apenas latas de 18 litros;
#     comprar apenas galões de 3,6 litros;
#     misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. 

from math import ceil

tamanho = int(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
litros_necessarios = tamanho / 6
litros_necessarios = litros_necessarios * 1.1 #folga de 10%

print(f"Litros necessários: {litros_necessarios:.2f}")

latas_necessarias = ceil(litros_necessarios / 18)
galoes_necessarios = ceil(litros_necessarios / 3.6)

print(f"Somente latas necessárias: {latas_necessarias}")
print(f"Somente galões necessárias: {galoes_necessarios}")
print(f"Preço somente latas: {(latas_necessarias *80):.2f}")
print(f"Preço somente galões: {(galoes_necessarios *25):.2f}")


#latas com galoes
latas_com_galoes = ceil(litros_necessarios // 18) #divisão inteira
litros_restantes = litros_necessarios % 18 #resto do que faltou
galoes_com_latas = ceil(litros_restantes / 3.6)
preco_latas_com_galoes = (latas_com_galoes * 80 )
preco_galoes_com_latas = (galoes_com_latas * 25)
preco_total = preco_latas_com_galoes + preco_galoes_com_latas

print(f"PREÇO LATAS EM CONJUNTO COM GALÕES: ")
print(f"Latas necessárias {latas_com_galoes}")
print(f"Galões necessárias {galoes_com_latas}")
print(f"Preço latas com galões: {preco_total:.2f}")
