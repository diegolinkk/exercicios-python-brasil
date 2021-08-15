# Quadrado mágico. 
# Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma.
#  Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

# 8  3  4 
# 1  5  9
# 6  7  2
# Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. 
# Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.


def verifica_quadrado_magico(lista):

    #o número mágico tem que ser igual em qualquer validação
    numero_magico = lista[0] + lista[1] + lista[2]
    eh_quadrado_magico = True #começa como true e faz as validações

    soma_linha_1 = lista[0] + lista[1] + lista[2]
    soma_linha_2 = lista[3] + lista[4] + lista[5]
    soma_linha_3 = lista[6] + lista[7] + lista[8]

    soma_coluna_1 = lista[0] + lista[3] + lista[6]
    soma_coluna_2 = lista[1] + lista[4] + lista[7]
    soma_coluna_3 = lista[2] + lista[5] + lista[8]

    soma_diagonal_1 = lista[0] + lista[4] + lista[8]
    soma_diagonal_2 = lista[2] + lista[4] + lista[6]

    somas = [] #junta tudo pra fazer uma iteração e validar
    somas.append(soma_linha_1)
    somas.append(soma_linha_2)
    somas.append(soma_linha_3)

    somas.append(soma_coluna_1)
    somas.append(soma_coluna_2)
    somas.append(soma_coluna_3)

    somas.append(soma_diagonal_1)
    somas.append(soma_diagonal_2)

    for soma in somas:
         if soma != numero_magico:
             eh_quadrado_magico = False

    return(eh_quadrado_magico)


lista = [8,3,4,1,5,9,6,7,2]
lista2 = [2,9,4,1,5,9,6,7,8]
print(verifica_quadrado_magico(lista))
print(verifica_quadrado_magico(lista2))