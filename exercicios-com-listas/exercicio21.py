# Faça um programa que carregue uma lista com os modelos de cinco veiculos (exemplo de modelos: FUSCA, GOL, VECTRA etc). 
# Carregue uma outra lista com o consumo desses veiculos, isto é, quantos quilômetros cada um desses veiculos faz com um litro de combustível. 
# Calcule e mostre:
# O modelo do veiculo mais econômico;
# Quantos litros de combustível cada um dos veiculos cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, 
# considerando um que a gasolina custe R$ 2,25 o litro. 
# Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo.
#  Os dados são fictícios e podem mudar a cada execução do programa.
# Comparativo de Consumo de Combustível

# Veículo 1
# Nome: fusca
# Km por litro: 7
# Veículo 2
# Nome: gol
# Km por litro: 10
# Veículo 3
# Nome: uno
# Km por litro: 12.5
# Veículo 4
# Nome: Vectra
# Km por litro: 9
# Veículo 5
# Nome: Peugeout
# Km por litro: 14.5

# Relatório Final
#  1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
#  2 - gol             -   10.0 -  100.0 litros - R$ 225.00
#  3 - uno             -   12.5 -   80.0 litros - R$ 180.00
#  4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
#  5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
# O menor consumo é do peugeout.

veiculos = []

while True:
    modelo = input("Digite o modelo do veículo ou 0 para sair: ")

    if modelo.lower() == '0':
        break

    consumo = float(input("Digite o consumo do veiculo: "))
    
    veiculos.append([modelo, consumo])

preco_gasolina = 2.25
distancia = 1000

mais_economico = veiculos[0]

contador = 1
for veiculo in veiculos:
    modelo = veiculo[0]
    consumo = veiculo[1]
    consumo_distancia = distancia / consumo
    print(f"{contador} - {modelo} - {consumo} - R${consumo_distancia:.2f} - R${consumo_distancia * preco_gasolina:.2f}")

    #comparando se é o mais econômico da lista
    consumo_distancia_economico = distancia / mais_economico[1]

    if consumo_distancia < consumo_distancia_economico:
        mais_economico = veiculo

print(f"O menor consumo é o {mais_economico[0]}")