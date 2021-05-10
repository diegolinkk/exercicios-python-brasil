#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Digite F para femininou ou M para masculino: ")

if sexo.lower() == 'f':
    print("Feminino")
elif sexo.lower() == 'm':
    print("Masculino")
else:
    print("Sexo inválido")