# Faça um programa com uma função chamada somaImposto. 
# A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, 
# que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.


def somaImposto(valor,taxa):
    taxa = taxa / 100 #receberemos um inteiro e transformaremos em percentual
    imposto = valor * taxa
    return valor + imposto


print(somaImposto(100,15))