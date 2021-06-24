#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado

def calcula_digito(numero):
    numero = str(numero)
    return len(numero)


print(calcula_digito(150123123123))
print(calcula_digito(100))
print(calcula_digito(1000))
print(calcula_digito(10000))