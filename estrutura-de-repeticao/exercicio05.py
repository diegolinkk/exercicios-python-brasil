#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
# Valide a entrada e permita repetir a operação.

populacao_a = int(input("Digite o tamanho da população A: "))
taxa_populacao_a = int(input("Digite a taxa de crescimento da população A (em %): "))

populacao_b = int(input("Digite o tamanho da população B: "))
taxa_populacao_b = int(input("Digite a taxa de crescimento da população B (em %): "))

repetir = True

while repetir:
    anos = 0

    if populacao_b > populacao_a and taxa_populacao_b > taxa_populacao_a:
        break

    while populacao_a < populacao_b:
        populacao_a += populacao_a * (taxa_populacao_a / 100)
        populacao_b += populacao_b * (taxa_populacao_b / 100)
        anos +=1
    
    print(f"Foram necessários {anos} anos para a população A ultrapassar a população B: " )

    pergunta_repetir = input("Repetir ? [s/n]: ")
    if pergunta_repetir.lower() == "s":
        repetir = True
        populacao_a = int(input("Digite o tamanho da população A: "))
        taxa_populacao_a = int(input("Digite a taxa de crescimento da população A: "))

        populacao_b = int(input("Digite o tamanho da população B"))
        taxa_populacao_b = int(input("Digite a taxa de crescimento da população B: "))
    else:
        repetir = False

print("Obrigado")
        