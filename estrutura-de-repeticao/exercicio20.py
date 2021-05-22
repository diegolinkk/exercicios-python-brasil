repetir = 's'
numero = 1

while repetir.lower() == 's':
    numero = int(input("Digite o valor que você deseja calcular o fatorial: "))
    if numero <=0 or numero > 16:
        print("Número inválido")
        break

    fatorial = numero
    multiplicador = numero -1
    
    while multiplicador >=1:
        fatorial *= multiplicador
        multiplicador -=1
    
    print(f"O fatorial de {numero} é: {fatorial}")
    repetir = input("Repetir ? [s/n]")