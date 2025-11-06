'''
Tuplas sao estruturas de dados muito parecidas com as listas , 
a principal diferença é que tuplas sao imutaveis enquanto listas sao mutaveis.

OBS: usar , (virgula) no vinal nas tuplas dentro de parenteses.
'''
# !Exemplo: 
frutas=("laranja", "pera", "uva",)

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)

#* Acessando os valores da tupla:

frutas[0] #maçã
frutas[2] #uva

#! Tuplas aninhadas:
'''Tuplas podem armazenar todos os tipos de objetos Python.
Portanto, tuplas podem armazenar outras tuplas. Criando Estruturas bidimensionais (tabelas)
'''
#* Exemplos:

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c")
)

matriz[0] #(1, "a", 2)
matriz[0][0] #1
matriz[0][-1] #2
matriz[-1][-1] #"c"

#! Fatiamento
#Podemos extrair um conjunto de valores de uma sequencia. Basta passar o indice inicial e/ou final parar acessar o conjunto.
#Alem disso, podemos infrmar quantas posiçoes o cursor deve "pular" no acesso

#* Exemplo:

tupla = ("p", "y", "t", "h", "o", "n")
tupla[2:] # ("t", "h", "o", "n")
tupla[:2] #("p", "y")
tupla[1:3] # ( "y", "t")
tupla[0:3:2] # ("p", "t")
tupla[::] # ("p", "y", "t", "h", "o", "n") 
tupla[::-1] # ("n", "o", "h", "t", "y", "p")

#! Iterar
#* Exemplo for

carros = ("gol", "celta", "palio")
for carro in carros:
    print(carro)
    
#* Exemplo enumerate:

carros = ("gol", "celta", "palio")
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")