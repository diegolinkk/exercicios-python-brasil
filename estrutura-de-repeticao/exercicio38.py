# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:

#     Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#     Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#     A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
#  Faça um programa que determine o salário atual desse funcionário. 
# Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário. 

ano_inicial = 1996
ano_final = 2001
percentual_de_aumento = 1.5
salario_inicial = float(input("Digite o salário inicial do funcionário: "))

salario_atual = salario_inicial + (salario_inicial * (percentual_de_aumento / 100))

for ano in range(ano_inicial,ano_final + 1):
    percentual_de_aumento *= 2
    salario_atual += salario_atual * (percentual_de_aumento / 100)

print(f"O salário atual é: {salario_atual:.2f}")