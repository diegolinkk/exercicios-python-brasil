# Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
#  No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. 
# O seu resultado fica sendo a média dos três valores restantes. 
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos 
# e depois informe a média dos saltos conforme a descrição acima informada 
# (retirar o melhor e o pior salto e depois calcular a média). 
# Faça uso de uma lista para armazenar os saltos. 
# Os saltos são informados na ordem da execução, portanto não são ordenados.
#  O programa deve ser encerrado quando não for informado o nome do atleta. 
# A saída do programa deve ser conforme o exemplo abaixo:

# Atleta: Rodrigo Curvêllo

# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Melhor salto:  6.5 m
# Pior salto: 5.3 m
# Média dos demais saltos: 5.9 m

# Resultado final:
# Rodrigo Curvêllo: 5.9 m

nome_atleta = input("Digite o nome do Atleta: ")

if nome_atleta:
    notas = []
    for nota in range(5):
        notas.append(float(input("Digite a nota de número: ")))
    
    print(f"Nome do Atleta: {nome_atleta}")
    print(f"Primeiro salto: {notas[0]}")
    print(f"Primeiro salto: {notas[1]}")
    print(f"Primeiro salto: {notas[2]}")
    print(f"Primeiro salto: {notas[3]}")
    print(f"Primeiro salto: {notas[4]}")

