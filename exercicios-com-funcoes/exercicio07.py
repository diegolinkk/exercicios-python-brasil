# Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
#  O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, 
# que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. 
# Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. 
# Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. 
# O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. 
# Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.


def calcula_multa(valor,dias_em_atraso):
    if dias_em_atraso == 0:
        return valor
    
    percentual_multa = 0.03
    percentual_multa += (0.001 *  dias_em_atraso)

    valor += valor * percentual_multa

    return valor


prestacoes = []

while True:
    valor = int(input("Digite o valor a ser pago ou 0 para terminar: "))

    if valor == 0:
        break

    dias_em_atraso = int(input("Digite os dias em atraso: "))

    prestacao = calcula_multa(valor,dias_em_atraso)
    print(prestacao)
    prestacoes.append(prestacao)


print("Relatório do dia")

prestacao_numero = 1

for prestacao in prestacoes:
    print(f"Prestação número {prestacao_numero} R${prestacao:.2f}")
    prestacao_numero +=1