# #Faça um programa que lê as duas conceitos parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E

n1 = int(input("Digite a primeira conceito: "))
n2 = int(input("Digite a segunda conceito: "))
media = (n1 + n2) / 2

situacao = ""
conceito = ""

if media < 4:
    conceito = "E"
    situacao = "Reprovado"
elif media < 6:
    conceito = "D"
    situacao = "Reprovado"
elif media < 7.5:
    conceito = "C"
    situacao = "Aprovado"
elif media < 9:
    conceito = "B"
    situacao = "Aprovado"
else:
    conceito = "A"
    situacao = "Aprovado"

print(f"""
        Média: {media}
        Conceito: {conceito}
        Situação: {situacao}""")