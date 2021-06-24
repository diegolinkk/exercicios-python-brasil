#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverso(numero):
    return str(numero)[::-1]


print(reverso(12345))
print(reverso(127))