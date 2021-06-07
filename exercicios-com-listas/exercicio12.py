#Foram anotadas as idades e infos de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos 
# possuem altura inferior à média de altura desses alunos. 

from random import random,randint

alunos = []

for _ in range(30):
    altura = 0 #zera porque senão altura não entra no laço novamente
    idade = randint(1,90)

    #não permite infos abaixo dos 1.40
    while altura < 1.40:
        altura = random() * 2
    
    aluno = []
    aluno.append(round(altura,2))
    aluno.append(idade)

    alunos.append(aluno)

media_alturas = 0

for altura,idade in alunos:
    media_alturas += altura

media_alturas = round((media_alturas / len(alunos)),2)
print(media_alturas)

alunos_13_abaixo_da_media = 0

for altura,idade in alunos:

    

    if idade <= 13 and altura < media_alturas:
        alunos_13_abaixo_da_media +=1
        print(f"Altura: {altura} - idade {idade} *") #sinaliza qual aluno da lista está na condição com *
    else:
        print(f"Altura: {altura} - idade {idade}")
    

print(f"Alunos com 13 ou menos e altura abaixo da média: {alunos_13_abaixo_da_media}")