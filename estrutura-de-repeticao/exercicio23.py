#Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados

numero = int(input("Digite um número: "))

for n in range(1,numero +1):
    #zera tudo
    divisor = n
    contador_divisoes_inteiras = 0
    numero_de_calculos = 0

    #faz os cálculos necessários para validar se é primo
    while divisor >=1:
        if n % divisor == 0:
            contador_divisoes_inteiras +=1

        numero_de_calculos +=1
        divisor -=1
    
    #verifica se de fato é primo de acordo com o cálculo acima
    if contador_divisoes_inteiras <=2:
        print(f"O número {n} é primo")
    else:
        print(f"O número {n} não é primo")
    
    print(f"Foram realizadas {numero_de_calculos} divisões para chegar a essa conclusão\n")
