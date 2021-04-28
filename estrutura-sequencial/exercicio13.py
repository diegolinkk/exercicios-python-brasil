# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7


altura = float(input("Digite sua altura: "))
peso_ideal_homens = (72.2 * altura) - 58
peso_ideal_mulheres = (62.1 * altura) - 44.7

print(f"Peso ideal para homens: {peso_ideal_homens:.2f}")
print(f"Peso ideal para mulheres: {peso_ideal_mulheres:.2f}")