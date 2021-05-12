# #As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = int(input("Digite seu salário: "))
percentual_aumento = 0

if salario <= 280:
    percentual_aumento = 20
elif salario <= 700:
    percentual_aumento = 15
elif salario <= 1500:
    percentual_aumento = 10
else:
    percentual_aumento = 5

valor_aumento = salario * (percentual_aumento / 100)
novo_salario = salario + valor_aumento

print(f"Salário antes do reajuste: R${salario:.2f}")
print(f"Percentual do aumento aplicado: {percentual_aumento}%")
print(f"Valor do aumento: R${valor_aumento:.2f}")
print(f"Novo salário: R${novo_salario:.2f}")