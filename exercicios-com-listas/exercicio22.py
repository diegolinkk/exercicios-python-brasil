# Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. 
# A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, 
# para verificar o que se pode aproveitar deles.

# Foi requisitado que você desenvolva um programa para registrar este levantamento. 
# O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
# necessita da esfera;
# necessita de limpeza; 
# necessita troca do cabo ou conector; 
# quebrado ou inutilizado 
# Uma identificação igual a zero encerra o programa.    
# Ao final o programa deverá emitir o seguinte relatório:
# Quantidade de mouses: 100

# Situação                        Quantidade              Percentual
# 1- necessita da esfera                  40                     40%
# 2- necessita de limpeza                 30                     30%
# 3- necessita troca do cabo ou conector  15                     15%
# 4- quebrado ou inutilizado              15                     15%

defeitos = [0,0,0,0,0]

while True:
    defeito = int(input("""Digite a situação do mouse:
    1 - necessita da esfera
    2 - necessita de limpeza
    3 - necessita troca do cabo ou conector
    4 - quebrado ou inutilizado
    0 - sair
    Digite sua opção: """))

    if defeito == 0:
        break

    if defeito >0 and defeito <=4:
        defeitos[defeito] +=1

total_de_defeitos = 0

for defeito in defeitos[1:]:
    total_de_defeitos += defeito

print("Situação \t\t\t quantidade \t percentual")
print(f"1 - necessita da esfera:\t\t {defeitos[1]}\t {(defeitos[1] / total_de_defeitos) * 100:.2f}% ")
print(f"2 - necessita da limpeza:\t\t {defeitos[2]}\t {(defeitos[2] / total_de_defeitos) * 100:.2f}% ")
print(f"3 - necessita de troca de cabo ou conector:{defeitos[3]}\t {(defeitos[3] / total_de_defeitos) * 100:.2f}% ")
print(f"4 - quebrado ou inutilizado:\t\t {defeitos[4]}\t {(defeitos[4] / total_de_defeitos) * 100:.2f}% ")
