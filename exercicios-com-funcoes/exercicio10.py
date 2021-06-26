# Jogo de Craps.
# Faça um programa de implemente um jogo de Craps. 
# O jogador lança um par de dados, obtendo um valor entre 2 e 12. 
# Se, na primeira jogada, 
# você tirar 7 ou 11, você um "natural" e ganhou. 
# Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". 
# Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.


from random import randrange


def craps():
    jogada = randrange(2,13)

    if jogada == 7 or jogada == 11:
        return (f" Você tirou {jogada} e ganhou na primeira jogada")
    elif jogada == 2 or jogada ==3 or jogada == 12:
        return (f"Você tirou {jogada} e perdeu na primeira rodada ")
    else:
        objetivo = jogada #o objetivo é tirar esse ponto novamente
        print(f"Seu objetivo é tirar {objetivo} novamente")

        while True:
            jogada = randrange(2,13)
            print(f"Você tirou {jogada}")

            #se tirar 7, perdeu o jogo
            if jogada == 7:
                return("Você tirou 7 e está fora do jogo")
                
            if jogada == objetivo:
                return (f"Parabéns, seu objetivo era tirar {objetivo} e você tirou {jogada} novamente")

print(craps())