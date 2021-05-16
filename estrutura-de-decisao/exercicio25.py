# #Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

pergunta1 = input("Telefonou para a vítima? ")
pergunta2 = input("Esteve no local do crime? ")
pergunta3 = input("Mora perto da vítima? ")
pergunta4 = input("Devia para a vítima? ")
pergunta5 = input("Já trabalhou com a vítima ? ")

nivel_suspeita = 0

if pergunta1 == "sim":
    nivel_suspeita +=1
if pergunta2 == "sim":
    nivel_suspeita +=1
if pergunta3 == "sim":
    nivel_suspeita +=1
if pergunta4 == "sim":
    nivel_suspeita +=1
if pergunta5 == "sim":
    nivel_suspeita +=1

if nivel_suspeita == 2:
    print("Suspeita")
elif nivel_suspeita == 3 or nivel_suspeita == 4:
    print("Cúmplice")
elif nivel_suspeita == 5:
    print("Assassino")
else:
    print("Inocente")