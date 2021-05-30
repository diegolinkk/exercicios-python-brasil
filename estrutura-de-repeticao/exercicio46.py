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
    saltos = []
    for salto in range(5):
        saltos.append(float(input("Digite a nota de número: ")))
    
    print(f"Nome do Atleta: {nome_atleta}")
    print(f"Primeiro salto: {saltos[0]}m")
    print(f"Primeiro salto: {saltos[1]}m")
    print(f"Primeiro salto: {saltos[2]}m")
    print(f"Primeiro salto: {saltos[3]}m")
    print(f"Primeiro salto: {saltos[4]}m")

    #encontrar o maior e o menor (sem auxílio de funções)

    indice_melhor_salto = 0
    indice_pior_salto = 0

    contador = 0

    for salto in saltos:
        if salto > saltos[indice_melhor_salto]:
            indice_melhor_salto = contador
        
        if salto < saltos [indice_pior_salto]:
            indice_pior_salto = contador

        contador +=1 


    melhor_salto = saltos[indice_melhor_salto]
    pior_salto = saltos[indice_pior_salto]

    saltos.remove(melhor_salto)
    saltos.remove(pior_salto)

    print(f"Melhor salto: {melhor_salto}m")
    print(f"Pior salto: {pior_salto}m")

    #calcula média dos demais saltos

    soma_saltos = 0
    for salto in saltos:
        soma_saltos += salto
    
    media_saltos = soma_saltos / len(saltos)

    print(f"Média dos demais saltos: {media_saltos:.1f}m")
    print(f"Resultado final: {media_saltos:.1f}m")