#São Operadores utilizados para comparar se os 2 objetos testados ocupam a mesma posição na memória.
#Exemplo:

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso
##Retorna True, pois ambos apontam para o mesmo objeto na memória.

curso is not nome_curso
##Retorna False, pois ambos apontam para o mesmo objeto na memória.

saldo is limite
##Retorna True, pois ambos apontam para o mesmo objeto na memória.

saldo = 1000
limite = 500

print(saldo is limite)
print(saldo is not limite)
