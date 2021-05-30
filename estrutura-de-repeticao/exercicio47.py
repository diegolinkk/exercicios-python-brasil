# Em uma competição de ginástica, cada atleta recebe notas de sete jurados. 
# A melhor e a pior nota são eliminadas. 
# A sua nota fica sendo a média dos notas restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta 
# em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). 
# As notas não são informados ordenadas. 
# 
# Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Aparecido Parente
# Nota: 9.9
# Nota: 7.5
# Nota: 9.5
# Nota: 8.5
# Nota: 9.0
# Nota: 8.5
# Nota: 9.7

# Resultado final:
# Atleta: Aparecido Parente
# Melhor nota: 9.9
# Pior nota: 7.5
# Média: 9,04

notas = []
nome_atleta = input("Digite o nome do atleta: ")
for nota_numero in range(1,8):
    nota = float(input(f"Digite o nota {nota_numero}: "))
    notas.append(nota)

print(f"Atleta: {nome_atleta}")
for nota in notas:
    print(f"Nota: {nota}")

melhor_nota = notas[0]
pior_nota = notas[0]

for nota in notas:
    if nota > melhor_nota:
        melhor_nota = nota

    if nota < pior_nota:
        pior_nota = nota

print(f"Melhor nota: {melhor_nota}")
print(f'"Pior nota: {pior_nota}')

notas.remove(melhor_nota)
notas.remove(pior_nota)

soma_notas = 0
for nota in notas:
    soma_notas += nota

print(f"Média: {soma_notas / len(notas):.2f}")