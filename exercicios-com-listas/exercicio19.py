# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade 
# de organizações:

# "Qual o melhor Sistema Operacional para uso em servidores?"

# As possíveis respostas são:

# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro

# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

# Sistema Operacional     Votos   %
# -------------------     -----   ---
# Windows Server           1500   17%
# Unix                     3500   40%
# Linux                    3000   34%
# Netware                   500    5%
# Mac OS                    150    2%
# Outro                     150    2%
# -------------------     -----
# Total                    8800

# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.

enquete = [
    ["0 - Sair", 0],
    ["Windows Server", 0],
    ["Unix", 0],
    ["Linux", 0],
    ["Netware", 0],
    ["Mac OS", 0],
    ["Outro", 0]
]

while True:
    voto = int(input("""
     "Qual o melhor Sistema Operacional para uso em servidores?"

    # As possíveis respostas são:

    1- Windows Server
    2- Unix
    3- Linux
    4- Netware
    5- Mac OS
    6- Outro
    0- Sair
    Digite sua resposta: """))

    if voto == 0:
        break

    #Adiciona o voto
    if voto >=1 and voto <=6:
        enquete[voto][1] +=1

total_votos = 0
for sistema,votos in enquete:
    total_votos += votos

print(total_votos)

mais_votado = enquete[1]

print("\nSistema Operacional Votos\t%")
print("*" * 50)
for sistema, votos in enquete[1:]:
    print(f"{sistema}\t\t{votos}\t{(votos / total_votos)*100:.1f}%")

    if votos > mais_votado[1]:
        mais_votado = [sistema,votos]


print("*" * 50)
print(f"O Sistema Operacional mais votado foi o {mais_votado[0]} " +
        F"com {mais_votado[1]} votos, correspondendo a {(mais_votado[1] / total_votos) * 100:.1f}% dos votos.")
