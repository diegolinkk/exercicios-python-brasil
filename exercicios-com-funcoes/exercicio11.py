#Data com mês por extenso. 
# Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. 
# Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

def data(string_data):

    meses = {
        1:"janeiro",
        2:"fevereiro",
        3:"março",
        4:"abril",
        5:"maio",
        6:"junho",
        7:"julho",
        8:"agosto",
        9:"setembro",
        10:"outubro",
        11:"novembro",
        12:"dezembro",
    }
    

    data_lista = string_data.split("/")
    dia = int(data_lista[0])

    if dia < 1 or dia > 31:
        return ("Data inválida")

    mes = int(data_lista[1]) 

    if mes in meses:
        mes = meses[mes]
    else:
        return("Data inválida xxxx")

    ano = data_lista[2]

    return(f"{dia} de {mes} de {ano}")



print(data("14/12/2021"))
print(data("14/04/2021"))