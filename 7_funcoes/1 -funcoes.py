'''
Função é um bloco de codigo identificado por um nome e pode 
receber uma lista de parametros, esses parametros podem ou nao ter valores padrao.
Usar funcoes torna o codigo mais legivel e possibilita o reaproveitamento de codigo.
Programar baseado em funcoes, é o mesmo que dizer que estamos programando de maneira estruturada!
'''

#! Exemplo:
def exibir_mensagem():
    print("Olá mundo!")
    
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")
    
def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")
    
exibir_mensagem()
exibir_mensagem_2(nome="Vitor")
exibir_mensagem_3()
exibir_mensagem_3(nome="Pandora")

#* Retornando valores
'''
Para retornar um valor, utilizamos a palavra reservada return.
Toda funcao retorna None por padrao. Diferente de outras linguagens de programação, em python, uma funcao pode retornar mais de um valor.
'''
#! Exemplo:

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    
    return antecessor, sucessor

print(calcular_total([10, 20, 34]))
print(retorna_antecessor_e_sucessor(10))


