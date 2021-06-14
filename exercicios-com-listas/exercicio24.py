# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . 
# Depois, mostre quantas vezes cada valor foi conseguido. 
# Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.

from random import randrange

#número da face : quantidade de vezes
vezes_dado = {
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
}

#simulando as jogadas
for _ in range(100):
    vezes_dado[randrange(1,7)] +=1


for face,quantidade in vezes_dado.items():
    print(f"Face - {face} Quantidade de vezes jogada: {quantidade}")