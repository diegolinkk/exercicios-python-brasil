# #Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';


nome = input("Digite seu nome (maior que 3 caracteres): ")

while len(nome) < 3:
    nome = input("Nome com menos de 3 letras, digite novamente: ")

idade = int(input("Digite sua idade (entre 0 e 150): "))

while idade < 0 or idade > 150:
    idade = int(input("Idade menor que 0 ou maior que 150, digite sua idade novamente: "))

salario = int(input("Digite seu salário(maior que 0): "))

while salario < 0:
    salario = int(input("Salário menor que zero, digite seu salário novamente: "))

sexo = input("Digite seu sexo (f ou m): ")

while sexo.lower() != 'f' and sexo.lower() != 'm':
    sexo = input("Sexo incorreto, digite seu sexo novamente: ")

estado_civil = input("Digite seu estado civil")

while estado_civil.lower() not in ['s','c','v','d']:
    estado_civil = input("Estado civil incorreto, digite seu estado civil novamente: ")





print("Todas as informações são válidas")