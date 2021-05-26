# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. 
# Foram obtidos os seguintes dados:

#     Código da cidade;
#     Número de veículos de passeio (em 1999);
#     Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
#     Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
#     Qual a média de veículos nas cinco cidades juntas;
#     Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

from random import randint

lista_cidades = []

#seed
for codigo_cidade in range(1,6):
    cidade = {}
    cidade["codigo"] = codigo_cidade
    cidade["veiculos_99"] = randint(1,5000)
    cidade["acidentes_99"] = randint(1,100)
    lista_cidades.append(cidade)

maior_indice = lista_cidades[0]
menor_indice = lista_cidades[0]

soma_veiculos = 0

soma_acidentes_2000_carros = 0
qtd_cidades_acidentes_2000_carros = 0

print("CIDADES")

for cidade in lista_cidades:
    print(cidade)
    if cidade["acidentes_99"] > maior_indice["acidentes_99"]:
        maior_indice = cidade
    if cidade["acidentes_99"] < menor_indice["acidentes_99"]:
        menor_indice = cidade
    
    soma_veiculos += cidade["veiculos_99"]

    #se tem menos de 2000 carros, coloca na estatística
    if cidade["veiculos_99"] <= 2000:
        soma_acidentes_2000_carros += cidade["acidentes_99"]
        qtd_cidades_acidentes_2000_carros +=1

#evitar divisão por 0
if qtd_cidades_acidentes_2000_carros == 0:
    qtd_cidades_acidentes_2000_carros = 1

media_veiculos = soma_veiculos / len(lista_cidades)
media_acidentes_menos_2000 = soma_acidentes_2000_carros / qtd_cidades_acidentes_2000_carros

print("\nESTATÍSTICAS")
print(f"Cidade com maior índice de acidentes: {maior_indice}")
print(f"Cidade com menor índice de acidentes: {menor_indice}")
print(f"Média de veículos em todas as cidades: {media_veiculos}")
print(f"Média de acidente em cidades com 2000 carros ou menos: {media_acidentes_menos_2000:.2f}")