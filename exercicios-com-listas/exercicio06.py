#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
#  imprima o número de alunos com média maior ou igual a 7.0. 

medias = []

for aluno in range(1,3):

    soma_notas = 0

    for nota in range(1,5):

        soma_notas += float(input(f"Digite a nota {nota} do aluno {aluno}: "))
    
    media = soma_notas / 4
    medias.append(media)

#RETORNE N TAL QUE N SEJA MAIOR OU IGUAL A 7.00 ENCONTRATO NO ITERÁVEL MEDIAS
notas_acima_de_7 = filter(lambda n: n >=7.00, medias)


print(f"Número de alunos com média maior ou igual a 7: {len(list(notas_acima_de_7))}")