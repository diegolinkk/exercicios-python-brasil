# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
# 1 , 2, 3, 4  - Votos para os respectivos candidatos 
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

from random import randint

urna = {
    1: {'nome':'Nolsobaro','votos': 0},
    2: {'nome':'Polvo','votos': 0},
    3: {'nome':'Circo','votos': 0},
    4: {'nome':'Amoeba','votos': 0},
    5: {'nome':'Brancos','votos': 0},
    6: {'nome':'Nulos','votos': 0},
}

votos_nulos = 0
total_de_votos = 0 #20 eleitores farão seus votos

while total_de_votos < 20:
    total_de_votos +=1
    voto = randint(1,8)
    
    if voto in urna:
        urna[voto]['votos'] +=1
    else:
        urna[6]['votos'] += 1

print("Apuração dos votos: ")

for candidato in urna.values():
    nome_candidato = candidato['nome']
    votos_candidato = candidato['votos']

    print(f'Nome do candidato: {nome_candidato} - votos: {votos_candidato}')

print(f"Percentual de votos em branco: {(urna[5]['votos'] / total_de_votos) * 100} %")
print(f"Percentual de votos nulos: {(urna[6]['votos'] / total_de_votos) * 100} %")