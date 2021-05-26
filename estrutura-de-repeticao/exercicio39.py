# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno 
# e o segundo representando a sua altura em centímetros. 
# Encontre o aluno mais alto e o mais baixo. 
# Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas. 


altura_aluno = float(input("Digite a altura do aluno: "))
codigo_aluno = int(input("Digite o código do aluno: "))

altura_aluno_mais_alto = altura_aluno
codigo_aluno_mais_alto = codigo_aluno

altura_aluno_mais_baixo = altura_aluno
codigo_aluno_mais_alto = codigo_aluno

for aluno in range(9):
    altura_aluno = float(input("Digite a altura do aluno: "))
    codigo_aluno = int(input("Digite o código do aluno: "))

    if altura_aluno > altura_aluno_mais_alto:
        altura_aluno_mais_alto = altura_aluno
        codigo_aluno_mais_alto = codigo_aluno
    
    if altura_aluno < altura_aluno_mais_baixo:
        altura_aluno_mais_baixo = altura_aluno
        codigo_aluno_mais_baixo = codigo_aluno


print(f"Aluno mais alto: código:{codigo_aluno_mais_alto} - peso:{altura_aluno_mais_alto}")
print(f"Aluno mais baixo: {codigo_aluno_mais_baixo} - {altura_aluno_mais_baixo}")