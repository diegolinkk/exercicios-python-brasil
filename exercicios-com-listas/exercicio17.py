# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
# O resultado do atleta será determinado pela média dos cinco valores restantes. 
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. 
# O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Rodrigo Curvêllo
 
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m

dados_gerais = []

while True:
    nome_atleta = input("Digite o nome do atleta ou nada para continuar: ")

    if not nome_atleta:
        break
    
    saltos = []

    for numero in range(1,6):
        saltos.append(float(input(f"Digite o valor do salto {numero}: ")))
    
    dados_atleta = []
    dados_atleta.append(nome_atleta)
    dados_atleta.append(saltos)

    dados_gerais.append(dados_atleta)

for nome, saltos in dados_gerais:

    print()
    print(f"Atleta: {nome}")
    print()

    print(f"Primeiro salto: {saltos[0]} m")
    print(f"Segundo salto: {saltos[1]} m")
    print(f"Terceiro salto: {saltos[2]} m")
    print(f"Quarto salto: {saltos[3]} m")
    print(f"Quinto salto: {saltos[4]} m")

    # Resultado final:
    # Atleta: Rodrigo Curvêllo
    # Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
    # Média dos saltos: 5.9 m

    print()
    print("Resultado final: ")
    print(f"Atleta: {nome} ")
    print(f"Saltos: {saltos[0]} - {saltos[1]} - {saltos[2]} - {saltos[3]} - {saltos[4]}")
    print(f"Média dos saltos: {sum(saltos) /  len(saltos):.2f} m")