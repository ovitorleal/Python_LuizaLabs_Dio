'''
SET's ou conjuntos são uma coleção que nao possui objetos repetidos,
Usamos sets para representar conjuntos matematicos ou eliminar itens duplicados
'''

#!Exemplo:

set([1,2,3,1,3,4]) #{1,2,3,4}

set("abacaxi") #{"b","a", "c", "x", "i"}

set(("palio", "gol", "celta", "palio")) #{"gol", "celta", "palio"}

# *Acessando os dados 
# Conjuntos em Python nao suportam indexaçao e nem fatiamento, caso queira acessar os valores é necessario converter o set em lista.

#!Exemplo:

numeros = {1,2,3,2}

numeros = list(numeros)

print(numeros[0])

#* for

carros = {"gol", "celta","palio"}

for carro in carros:
    print(carro)

# * Enumerate

carros = {"gol", "celta","palio"}

for indice,carro in enumerate(carros):
    print(f"{indice}: {carro}")