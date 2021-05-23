#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de 
# idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

continuar = 's'
soma = 0
numero_de_pessoas = 0

while continuar.lower() == 's':
    idade = int(input("Digite a idade da pessoa: "))
    soma += idade
    numero_de_pessoas += 1
    continuar = input("Continuar? [s/n]: ")

idade_media = idade / numero_de_pessoas

if idade_media <= 25:
    print("A turma é idosa")
elif idade_media  <= 60:
    print("A turma é adulta")
else:
    print("A turma é idosa")
