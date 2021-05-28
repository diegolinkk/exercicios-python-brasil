# O cardápio de uma lanchonete é o seguinte:
# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00

# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
# Considere que o cliente deve informar quando o pedido deve ser encerrado.

itens = {
    100: ("Cachorro Quente", 1.20),
    101: ("Bauru Simples", 1.30),
    102: ("Bauru com ovo", 1.50),
    103: ("Hambúrguer", 1.20),
    104: ("Cheeseburguer", 1.30),
    105: ("Refrigerante", 1.00),
}

pedido = []

while True:
    codigo = int(input("Digite um número da tabela ou 0 para sair: "))

    if codigo == 0:
        break

    quantidade = int(input("Digite a quantidade desejada: "))
    pedido.append((codigo,quantidade))


print(f"{'codigo'} {'Item'} {'Valor Unitário':>32} {'Quantidade':>14} {'Total':>8}")

valor_total_pedido = 0.0

for codigo_item,quantidade in pedido:
    if codigo_item in itens:
        nome_item = itens[codigo_item][0]
        valor_unitario = itens[codigo_item][1]
        quantidade = float(quantidade)
        valor_total_item = valor_unitario * quantidade
        valor_total_pedido += valor_total_item
        print(f"{codigo_item} {nome_item:>15} {valor_unitario:>15.2f} {quantidade:>15.0f} {valor_total_item:>15.2f}")

print(f"Valor total do pedido: R$ {valor_total_pedido:>41.2f}")
