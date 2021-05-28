# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão 
# e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). 
# Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
# Maior e Menor Acerto;
# Total de Alunos que utilizaram o sistema;
# A Média das Notas da Turma.
# Gabarito da Prova:

# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A
# Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.

#professor digita o próprio gabarito
gabarito = {}
for resposta in range(1,11):
    gabarito[resposta] = input(f"Digite a resposta {resposta} para o gabarito: ").upper()


#condicional para continuar adicionando alunos
continuar = 's'
notas_gerais = [] #soma todas as notas para fazer balanço no final

while continuar.lower() == 's':
    respostas_aluno = []

    #aluno respondendo
    for pergunta in range(1,11):
        resposta = input(f"Digite a resposta da pergunta {pergunta}: ")
        respostas_aluno.append(resposta)

    #avaliação do gabarito
    nota_aluno = 0
    questao_numero = 1

    for resposta in respostas_aluno:
        if resposta.upper() == gabarito[questao_numero]:
            nota_aluno +=1
        questao_numero +=1
    
    #adiciona aluno às notas gerais
    notas_gerais.append(nota_aluno)

    continuar = input("Continuar ? [s/n]")


#balanço de todas as notas

maior_nota = notas_gerais[0]
menor_nota = notas_gerais[0]
soma_de_notas = 0

for nota in notas_gerais:
    if nota > maior_nota:
        maior_nota = nota

    if nota < menor_nota:
        menor_nota = nota
    
    soma_de_notas += nota

media_de_notas = soma_de_notas / len(notas_gerais)

print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")
print(f"Quantidade de alunos: {len(notas_gerais)}")
print(f"Média de notas: {media_de_notas}")
    