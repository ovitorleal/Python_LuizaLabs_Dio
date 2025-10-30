#Range é uma função built-in do Python, é usada para produzir uma sequencia de numeros inteiros a partir de um inicio para um fim. 
#Se usarmos range (i,j) será produzido: i, i+1, i+2,..., j-1
#Ela recebe 3 argumentos: start (inicio) - opcional-, stop (fim) é exclusivo!!! - obrigatorio- e step (passo) -opcional-.
#Exemplo range com for:
for numero in range(0,11):
    print(numero, end=" ")
    
#tabuada do 5 usando range
for numero in range(0, 51, 5): #0 - start; 51 - stop; 5 - step
    print(numero, end=" ")