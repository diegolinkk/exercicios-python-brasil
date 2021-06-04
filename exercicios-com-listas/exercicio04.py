#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes. 

letras = []
vogais = ['a','e','i','o','u']
numero_de_consoantes = 0

for _ in range(10):
    letras.append(input("Digite uma letra: "))

for letra in letras:
    if letra not in vogais:
        numero_de_consoantes += 1
    

print(f"Foram digitadas {numero_de_consoantes} consoantes")