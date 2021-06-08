# #Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

valores = []

while True:
    valor = int(input("Digite um valor inteiro ou -1 para sair: "))

    if valor == -1:
        break

    valores.append(valor)

print("Valores em ordem normal:",end = " ")
for valor in valores:
    print(valor, end=' ')

print("\nValores em ordem reversa:", end = " ")

for valor in reversed(valores):
    print(valor,end=' ')

print()

print(f"Soma dos valores: {sum(valores)}")

media = sum(valores) / len(valores)
print(f"Média dos valores: {media}")

valores_acima_da_media = [valor for valor in valores if valor > media]
valores_abaixo_de_sete = [valor for valor in valores if valor < 7 ]

print(f"Valores acima da média: {valores_acima_da_media}")
print(f"Valores abaixo de sete: {valores_abaixo_de_sete}")

print("Fim do programa")
