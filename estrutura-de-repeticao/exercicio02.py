#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = input("Digite o nome do usuário: ")
senha = input("Digite a senha: ")

while usuario == senha:
    print("Valor inválido - usuário e senha não podem ser iguais")
    usuario = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")

print("Você digitou corretamente")