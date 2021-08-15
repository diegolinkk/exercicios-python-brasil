# Desenha moldura. 
# Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. 
# Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. 
# Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.

def desenha_moldura(linha = 1, coluna = 1):
    print("+",end="")

    for coluna in range(coluna):
        print("-",end="")
    
    print("+")

    for linha in range(linha -1):
        print("|",end="")

        for coluna in range(coluna + 1):
            print(" ",end="")  

        print("|")
    
    print("+",end="")

    for coluna in range(coluna + 1):
        print("-",end="")
    
    print("+")

desenha_moldura(4,4)
desenha_moldura(15,2)
desenha_moldura(33,100)
