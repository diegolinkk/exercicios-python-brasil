# #Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades

numero = int(input("Digite um número inteiro menor que 1000: "))

centenas = numero // 100
dezenas = (numero % 100) // 10
unidades = (numero % 100) % 10

texto_centenas = "centenas" if centenas > 1 else "centena"
texto_dezenas = "dezenas" if dezenas > 1 else "dezena"
texto_unidades = "unidades" if unidades > 1 else "unidade"

print(f"{centenas} {texto_centenas}, {dezenas} {texto_dezenas} e {unidades} {texto_unidades}")