# Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

from math import ceil

tamanho = int(input("Digite o tamanho da área a ser pintada: "))
litros_necessarios = ceil(tamanho / 3)
latas_necessarias = ceil(litros_necessarios / 18)
preco = latas_necessarias * 80


print(f"Litros necessários: {litros_necessarios} ")
print(f"Latas necessárias: {latas_necessarias} ")
print(f"Preço: R${preco:.2f} ")