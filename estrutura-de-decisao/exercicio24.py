# #Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

operacao = input("Digite qual operação você deseja realizar (digite: + - * ou /): ")

if operacao == "+":
    resultado = n1 + n2
elif operacao == "-":
    resultado = n1 - n2
elif operacao == "*":
    resultado = n1 * n2
elif operacao == "/":
    resultado = n1 / n2
else: #qualquer outro resultado vai retornar a soma
    resultado = n1 + n2

print(f"O resultado da operação é: {resultado}")

if resultado % 2 == 0:
    print("O resultado é par")
else:
    print("O resultado é impar")

if resultado < 0:
    print("O resultado é negativo")
else:
    print("O resultado é positivo")

if round(resultado) == resultado:
    print("O resultado é inteiro")
else:
    print("O resultado é decimal")