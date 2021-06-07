#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada. 

vetor_1 = []
vetor_2 = []
vetor_3 = []

for i in range(10):
    vetor_1.append(int(input("Digite um número inteiro: ")))
    vetor_2.append(int(input("Digite outro número inteiro: ")))
    vetor_3.append(int(input("Digite outro número inteiro: ")))

vetor_mesclado = []

for i in range(len(vetor_1)):
    vetor_mesclado.append(vetor_1[i])
    vetor_mesclado.append(vetor_2[i])
    vetor_mesclado.append(vetor_3[i])

print(vetor_mesclado)