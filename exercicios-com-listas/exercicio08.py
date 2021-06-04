# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
# Imprima a idade e a altura na ordem inversa a ordem lida.

idades = []
alturas = []

for _ in range(5):
    idades.append(int(input("Digite a idade: ")))
    alturas.append(float(input("Digite a altura: ")))


for i in range(len(idades) -1,-1, -1):
    print(f"Altura: {alturas[i]} ")
    print(f"Idade: {idades[i]}")
    print("")