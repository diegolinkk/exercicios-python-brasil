#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho_arquivo_megabytes = int(input("Digite o tamanho do arquivo a ser baixado: "))
velocidade_internet= int(input("Digite a velocidade da internet: "))

tamanho_arquivo_megabits = tamanho_arquivo_megabytes * 8

segundos_necessarios = tamanho_arquivo_megabits /  velocidade_internet

minutos = segundos_necessarios // 60
segundos = segundos_necessarios % 60

print(segundos_necessarios)
print(f"Vai levar {minutos:.0f} minutos e {segundos:.0f} segundos")