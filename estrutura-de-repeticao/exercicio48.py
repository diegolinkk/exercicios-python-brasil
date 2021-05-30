# Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
# Exemplo:
#   12376489
#   => 98467321

numero = input("Digite um número inteiro positivo: ")
numero_invertido = ""

for elemento in range(len(numero),0,-1):
    #aqui o índice começa no tamanho do array e termina no 1, na vdd queremos o ultimo elemento do array e terminar no 0
    elemento = elemento -1 
    numero_invertido += numero[elemento]



print(numero_invertido)
print(numero[::-1]) #posso fazer assim também (slice do começo ao fim com passo invertido) fonte - https://stackoverflow.com/questions/509211/understanding-slice-notation