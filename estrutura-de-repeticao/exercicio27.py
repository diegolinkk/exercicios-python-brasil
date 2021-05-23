#Faça um programa que calcule o número médio de alunos por turma. 
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.


numero_de_turmas = int(input("Digite o número de turmas: "))
total_de_alunos = 0
contador_de_turmas = 0

for turma in range(numero_de_turmas):
    alunos_por_turma = 0
    contador_de_turmas +=1
    alunos_por_turma = int(input(f"Digite o número de alunos para a turma {contador_de_turmas}: "))

    while alunos_por_turma > 40:
        print("Cada turma não pode ter mais de 40 alunos, digite novamente!!")
        alunos_por_turma = int(input(f"Digite o número de alunos para a turma {contador_de_turmas}: "))

    total_de_alunos += alunos_por_turma

media_de_alunos_por_turma = total_de_alunos / numero_de_turmas

print(f"A média de alunos por turma é de: {media_de_alunos_por_turma}")