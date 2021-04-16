#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = int(input("Digite a área do quadrado: "))
area = lado ** 2
print("O dobro da área é: {}".format(area * 2))