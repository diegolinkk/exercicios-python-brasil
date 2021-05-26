# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, 
# o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, 
# sua altura e seu peso. 
# O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
# Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, 
# além da média das alturas e dos pesos dos clientes

class Cliente():
    def __init__(self):
        self.codigo = None
        self.altura = None
        self.peso = None
    
    def __str__(self):
        return(f"Código: {self.codigo} - Peso: {self.peso} - Altura: {self.altura}")


codigo = 1 #valor aleatório

clientes = [] # lista de clientes

while True:
    continuar = input("\nDigite 0 para sair ou qualquer tecla para continuar: ")
    
    if continuar == '0':
        break

    codigo +=1

    c = Cliente()
    c.codigo = codigo
    c.altura = float(input("Digite a altura do cliente: "))
    c.peso = float(input("Digite o peso do cliente: "))
    clientes.append(c)

#para fazer a média posteriormente
soma_pesos = float(0)
soma_altura = float(0)

#atribui tudo ao primeiro cliente e depois evolui
cliente_mais_pesado = clientes[0]
cliente_mais_leve = clientes[0]
cliente_mais_alto = clientes[0]
cliente_mais_baixo = clientes[0]

for cliente in clientes:
    
    if cliente.peso > cliente_mais_pesado.peso:
        cliente_mais_pesado = cliente
    
    if cliente.peso < cliente_mais_leve.peso:
        cliente_mais_leve = cliente
    
    if cliente.altura > cliente_mais_alto.altura:
        cliente_mais_alto = cliente
    
    if cliente.altura < cliente_mais_baixo.altura:
        cliente_mais_baixo = cliente
    
    soma_pesos += cliente.peso
    soma_altura += cliente.altura


print(f"Cliente mais pesado: {cliente_mais_pesado}\n")
print(f"Cliente mais leve: {cliente_mais_leve}\n")
print(f"Cliente mais alto: {cliente_mais_alto}\n")
print(f"Cliente mais baixo: {cliente_mais_baixo}\n")
print(f"Média de pesos: {soma_pesos / len(clientes)}\n")
print(f"Média de alturas: {soma_altura / len(clientes)}\n")