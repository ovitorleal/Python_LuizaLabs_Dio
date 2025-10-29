#São operadores utilizados em conjunto com os operadores de comparação para combinar expressões lógicas.
#quando um operador de comparação é utilizado, o resultado retornado é um valor booleano (True ou False).
#Dessa forma podemos combinar operadores de comparação com operadores lógicos.
#Ex.: op_comparacao + op_logico + op_comparacao ... N ...

saldo = 1000
saque = 200
limite = 100

#Operador lógico "and" (e) => Retorna True se ambas as expressões forem verdadeiras.
saldo>= saque and saque <= limite
##Retorna False, pois a segunda expressão é falsa.

#Operador lógico "or" (ou) => Retorna True se ao menos uma das expressões for verdadeira.
saldo>= saque or saque <= limite
##Retorna True, pois a primeira expressão é verdadeira.

#Operador lógico "not" (não) => NEGAÇÃO!!! INVERSO.
not 1000 > 1500
##Retorna True, pois a expressão 1000 > 1500 é falsa.
contatos_emergencia = []
not contatos_emergencia
##Se a variável contatos_emergencia for vazia (False), o operador not retornará True.

not "saque 1500;"
##Retorna False, pois a string não está vazia.

not ""
##Retorna True, pois a string está vazia.

#PARENTESES SÃO IMPORTANTES!!!
saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo>= saque and saque <= limite or conta_especial and saldo>= saque
##Retorna True, pois a última expressão é verdadeira.
print (exp)
#ORGANIZANDO COM PARENTESES
exp_2 = (saldo>= saque and saque <= limite) or (conta_especial and saldo>= saque)
##Retorna True, pois a última expressão é verdadeira.
print (exp_2)





