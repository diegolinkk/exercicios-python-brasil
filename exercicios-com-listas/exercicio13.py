#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, 
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

from random import random

temperaturas = []

#gerando dados
for mes in range(1,13):
    infos_mes = []
    mes = mes
    temperatura_mes = round(random() * 50,2)
    
    infos_mes.append(mes)
    infos_mes.append(temperatura_mes)
    temperaturas.append(infos_mes)


media_anual_temperaturas = 0

for mes, temperatura in temperaturas:
    media_anual_temperaturas += temperatura

media_anual_temperaturas = round(media_anual_temperaturas / len(temperaturas),2)
print(media_anual_temperaturas)

meses = ['indefinido','janeiro','fevereiro','março', 'abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']

print("Meses com temperatura acima da média: ")
for mes, temperatura in temperaturas:
    if temperatura > media_anual_temperaturas:
        print(f"{mes} - {meses[mes]} - Temperatura: {temperatura:.1f} C ")