# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

#                           Até 5 Kg           Acima de 5 Kg
#     File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#     Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#     Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

#     Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente 
# receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a 
# quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: 
# tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar. 

tipo_carne = input("Digite qual carne você quer:\nF - Filé Duplo \nA - Alcatra \nP - picanha: ")
quilos = int(input("Digite quantos quilos você quer: "))
compra_no_cartao = input("Compra no cartão tabajara ? (S/N): ")

if tipo_carne.upper() == "F":
    texto_carne = "Filé Duplo"
    if quilos <=5:
        preco_por_quilo = 4.9
    else:
        preco_por_quilo = 5.80
elif tipo_carne.upper() == "A":
    texto_carne = "Alcatra"
    if quilos <=5:
        preco_por_quilo = 5.90
    else:
        preco_por_quilo = 6.80
else:
    texto_carne = "Picanha"
    if quilos <=5:
        preco_por_quilo = 6.90
    else:
        preco_por_quilo = 7.80

total = quilos * preco_por_quilo

if compra_no_cartao.upper() == "S":
    desconto = 5
else:
    desconto = 0

total -= desconto / 100

texto_cartao = "Cartão Tabajara" if compra_no_cartao.upper() == "S" else "Dinheiro"
print(f"Carne a ser comprada: {texto_carne}")
print(f"Forma de pagamento {texto_cartao}")
print(f"Desconto: {desconto}%")
print(f"Preço total: {total:.2f}")
