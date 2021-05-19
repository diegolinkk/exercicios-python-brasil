# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
#  e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país 
# A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. 

populacao_a  = 80000
populacao_b = 200000

anos = 0

while populacao_a < populacao_b:
    populacao_a += populacao_a * 0.03
    populacao_b += populacao_b * 0.0015
    anos +=1

print(f"Foram necessários {anos} anos para a população A passar a população B")