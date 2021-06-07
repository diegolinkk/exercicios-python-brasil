# #Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

#     "Telefonou para a vítima?"
#     "Esteve no local do crime?"
#     "Mora perto da vítima?"
#     "Devia para a vítima?"
#     "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

respostas = []

p1 = input("Telefonou para a vitima ? [s/n]: ")
p2 = input("Esteve no local do crime? [s/n]: ")
p3 = input("Mora perto da vítima ? [s/n]: ")
p4 = input("Devia para a vítima ? [s/n]: ")
p5 = input("Já trabalhou com a vítima ? [s/n]: ")

respostas.append(p1)
respostas.append(p2)
respostas.append(p3)
respostas.append(p4)
respostas.append(p5)

contador = 0

for resposta in respostas:
    if resposta.lower() == "s":
        contador +=1

if contador < 2:
    print("Inocente")
elif contador == 2:
    print("Suspeita")
elif contador <= 4:
    print("Cúmplice")
else:
    print("Assassino")