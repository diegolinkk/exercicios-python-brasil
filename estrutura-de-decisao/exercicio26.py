# #Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro 
# Escreva um algoritmo que leia o número de litros vendidos, 
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

preco_gasolina = 2.50
preco_alcool = 1.90
valor_a_pagar = 0

combustivel = input("Digite o tipo de combustível: Digite G para gasolina ou A para alcool")
litros = int(input("Digite quantos litros você quer: "))

if combustivel.upper() == "A":
    print("O combustível selecionado foi alcool")
    if litros <= 20:
        preco_alcool = preco_alcool * (97/100)
        print(f"Valor por litro: R${preco_alcool:.2f}")
        valor_a_pagar = preco_alcool * litros
    else:
        preco_alcool = preco_alcool * (95/100)
        print(f"Valor por litro: R${preco_alcool:.2f}")
        valor_a_pagar = preco_alcool * litros
else: #gasolina
    print("O combustível selecionado foi gasolina")
    if litros <= 20:
        preco_gasolina = preco_gasolina * (96/100)
        print(f"Valor por litro: R${preco_gasolina:.2f}")
        valor_a_pagar = preco_gasolina * litros
    else:
        preco_gasolina = preco_gasolina * (94/100)
        print(f"Valor por litro: R${preco_gasolina:.2f}")
        valor_a_pagar = preco_gasolina * litros

print(f"Quantidade de litros: {litros}")
print(f"Valor total a pagar: R${valor_a_pagar:.2f}")
