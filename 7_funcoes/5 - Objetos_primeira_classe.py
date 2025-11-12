'''
Em phyton tdo é objeto, dessa forma, funcoes tambem sao objetos.
Com isso podemos atribuir funcoes a variaveis, passa-las como parametro para funcoes, usa-las como valores em estruturas de dados
(listas, tuplas, dict, etc) e usar como valor de retorno para uma funcao(closures)
'''

#! Exemplo:

def somar(a,b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")
    
exibir_resultado(10, 10, somar)
