#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa 
# que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

temperatura = float(input("Digite a temperatura ou 0 para sair: "))

maior = temperatura
menor = temperatura
soma  = temperatura
contador = 1

while temperatura != 0:
    temperatura = float(input("Digite a temperatura ou 0 para sair: "))

    if temperatura > maior:
        maior = temperatura
    
    if temperatura < menor and temperatura != 0:
        menor = temperatura
    
    soma += temperatura
    contador +=1

print(f"A maior temperatura foi: {maior}")
print(f"A menor temperatura foi: {menor}")
print(f"A média de temperatura foi: {(soma / contador):.2f}")