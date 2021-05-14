#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    if ano % 100 != 0:
        print("O ano é bisexto")
    elif ano % 400 == 0:
        print("O ano é bisexto")
    else:
        print("O ano não é bisexto")
elif ano % 400 == 0:
    print("O ano é bisexto")
else:
    print("O ano não é bisexto")