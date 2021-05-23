#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.

quantidade_de_cds = int(input("Digite a quantidade de cds: "))
valor_total = 0
contador_cd = 0

for cd in range(quantidade_de_cds):
    contador_cd +=1
    valor_cd = int(input(f"Digite o valor do CD{contador_cd}:"))
    valor_total += valor_cd


valor_medio = valor_total / quantidade_de_cds

print(f"O valor médio dos CDs é de : R${valor_medio:.2f}")