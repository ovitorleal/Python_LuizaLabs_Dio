#Tecnica utilizada para retornar substrings (partes de uma string original), 
#informando o inicio (start), o fim (stop) e o passo (step) : [start:stop:[, step]].

#Exemplo: 
nome = "Vitor da Silva Leal"
print(nome [0]) #retorna o caractere na posição 0
print(nome [:5]) #sem informar o start, ele inicia do 0
print(nome [6:]) #sem informar o stop, ele vai até o final da string
print(nome [9:14]) #retorna da posição 9 até a 13 (o 14 não é incluso)
print(nome [0:5:2]) #retorna da posição 0 até a 4, pulando de 2 em 2
print(nome[:]) #retorna a string completa
print(nome[::-1]) #inverte a string, começando do final até o início, pulando de 1 em 1
