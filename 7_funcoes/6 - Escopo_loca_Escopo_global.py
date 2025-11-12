'''
Python trabalha com escopo local e global, dentro da funcao o escopo é local.
Portanto alterações ali feitas em objetos imutaveis serao perdidas quando o metodo terminar de ser executado.
Para usar objetos globais utilizamos a palvara-chave GLOBAL, que informa ao interpretador que a variavel esta sendo manipulada.
Essa NÃO É UMA BOA PRATICA E DEVE SER EVITADA.
'''

#! Exemplo:

salario = 2000

def salario_bonus(bonus):
    global salario
    salario+= bonus
    return salario

print(salario_bonus(500))

