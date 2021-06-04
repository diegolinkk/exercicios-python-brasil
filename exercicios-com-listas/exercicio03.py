#Faça um Programa que leia 4 notas, mostre as notas e a média na tela. 

notas = []
for nota in range(4):
    notas.append(int(input("Digite a nota: ")))

for nota in notas:
    print(nota)

media = sum(notas) / len(notas)

print(f"A média das notas é: {media}")