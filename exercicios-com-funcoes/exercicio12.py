#Embaralha palavra. 
# Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. 
# Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. 
# Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.

from random import shuffle

def embaralha_palavras(palavra):
    palavra = list(palavra)
    shuffle(palavra)
    return "".join(palavra)

print(embaralha_palavras("Cachorro"))
print(embaralha_palavras("Python"))
print(embaralha_palavras("Meu cachorro caiu"))