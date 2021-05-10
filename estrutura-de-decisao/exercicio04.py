#Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 

vogais = ['a','e','i','o','u']

letra = input("Digite uma letra: ")

if letra in vogais:
    print("A letra digitada é vogal")
else:
    print("A letra digitada é consoante")