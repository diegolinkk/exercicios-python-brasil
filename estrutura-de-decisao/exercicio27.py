# Uma fruteira está vendendo frutas com a seguinte tabela de preços:

#                           Até 5 Kg           Acima de 5 Kg
#     Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#     Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

#     Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
# receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) 
# de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente. 

kilos_morango = int(input("Quantos Kg de morango você quer ? "))
kilos_maca = int(input("Quantos Kg de mação você quer ?"))

if kilos_morango <= 5:
    preco_morango = 2.50
else:
    preco_morango = 2.20

if kilos_maca <= 5:
    preco_maca = 1.80
else:
    preco_maca = 1.50

valor_total = (kilos_morango * preco_morango) + (kilos_maca * preco_maca)

if valor_total >=25 or (kilos_morango  + kilos_maca) >=8:
    print("Desconto aplicado de 10%")
    valor_desconto = valor_total * (10 /100)
else:
    valor_desconto = 0

valor_total -= valor_desconto

print(f"O total a pagar é {valor_total:.2f}")