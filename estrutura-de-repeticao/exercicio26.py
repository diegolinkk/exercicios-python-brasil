#Numa eleição existem três candidatos. 
# Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

votos_candidato_1 = 0
votos_candidato_2 = 0
votos_candidato_3 = 0

numero_de_eleitores = int(input("Digite o número de eleitores: "))

for eleitor in range(numero_de_eleitores):
    voto = int(input("Votação 2021: \n 1 - para candidato 1\n 2 - para candidato 2\n 3 - para candidato 3\nDigite seu voto: "))
    if voto == 1:
        votos_candidato_1 +=1
    
    if voto == 2:
        votos_candidato_2 +=1
    
    if voto == 3:
        votos_candidato_3 +=1


print("APURAÇÃO DOS VOTOS")
print(f"Votos candidato 1: {votos_candidato_1}")
print(f"Votos candidato 2: {votos_candidato_2}")
print(f"Votos candidato 3: {votos_candidato_3}")