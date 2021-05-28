# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:
# Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
# 1       0
# 3       10
# 6       15
# 9       20
# 12      25
# Exemplo de saída do programa:
# Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
# R$ 1.000,00     0               1                       R$  1.000,00
# R$ 1.100,00     100             3                       R$    366,00
# R$ 1.150,00     150             6                       R$    191,67


valor_da_divida = float(input("Digite o valor da dívida: R$"))

parcelas_juros = {
    1:0,
    3:10,
    6:15,
    9:20,
    12:25
}

texto_divida = "Valor da Dívida"
texto_juros = "Valor dos Juros"
texto_qtd_parcela = "Quantidade de Parcelas"
texto_valor_parcela = "Valor da Parcela"

print(f"{texto_divida} {texto_juros:>20} {texto_qtd_parcela:>20} {texto_valor_parcela:>20}")

for parcelas,juros in parcelas_juros.items():
    divida_com_juros = valor_da_divida + (valor_da_divida * juros)
    print(f"R$ {divida_com_juros:.2f} {juros:>20} {parcelas:>20} {(divida_com_juros / parcelas):>20.2f}") 
    