'''Listas em Python podem armazenar de maneira sequencial qualquer tipo de objeto.
Podemos criar listas usando o construtot list, a função range ou colocando os valore separados por vírgulas entre colchetes.
Listas sao objetos mutaveis, por isso podemos alterar seus valores apos a criacao. 
'''
# !Exemplos 

fruta = ["laranaja", "maca", "uva"]
frutas = []
letras = list("python")
numeros = list(range(10))
carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]

print (fruta)
print(fruta[2])
print (frutas)
print(letras)
print(numeros)
print(carro)

'''
Sequencias suportam idenxação negativa. A contagem começa com -1
'''
# !Exemplo:
frutas = ["maçã", "laranja", "uva", "pera"]
# *frutas[-1] => pera
# *frutas[-3] => laranja

'''
Listas aninhadas
Listas podem armazenar todos os tipos de objetos em Python, entao podemos ter listas que armazenam outras listas
Com isso podemos criar estruturas bidimensionais (tabelas) e acessar informando os indices de linha e coluna.
'''

# !Exemplo:
matriz = [
    [1, "a", 2],
    ["b", 3, 4],   #MATRIZ 3X3
    [6, 5, "c"]   
]

print(matriz[0])    #pegando só a linha 0
print(matriz[0][0]) #linha 0 coluna 0
print(matriz[0][-1])
print(matriz[-1][-1])

'''
Fatiamento.
Alem de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequencia.
Para isso basta passar o indice inicial e/ou final para acessar o conjunto;
Podemos ainda informar quantas posições o cursor deve "pular" no acesso.
'''

# !Exemplo : 

lista = [ "p", "y", "t", "h", "o", "n"]
print(lista[2:]) # ["t", "h", "o", "n"]
print(lista[:2]) # ["p", "y"]
print(lista[0:3:2]) # ["p", "t"]
print(lista[::]) # [ "p", "y", "t", "h", "o", "n"]
print(lista[::-1]) # ["n", "o", "h", "t", "y", "p"]

'''
Iterar listas
A forma mais comum para percorrer os dados de uma lista é utilizando o comando for
'''
# !Exemplo:

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


'''
Função Enumerate
As vezes é necessario saber o indice do objeto dentro do laço for. Para isso podemos usar a funçao enumerate.
'''

# !Exemplo:

carros = ["gol", "celta", "palio"]

for indice, caro in enumerate(carros):
    print(f"{indice}: {carro}")

## COmpreensao de listas com filtros;

# ! Exemplo

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero%2==0:
        pares.append(numero)
        print(numero)

# Outra opção de filtro

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(numero)

##Modificando numeros

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
    print(numero)




