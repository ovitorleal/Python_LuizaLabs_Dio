#Estruturas de repetição sao utilizadas para repetir um trecho de codigo um determinado numero de vezes.
#Esse numero pode ser conhecido previamente ou determinado por uma expressao logica.

#Exemplo sem estrutura de repetição:
# Receba um numero do teclado e exibe o numeor e os 2 numeros seguintes.
a = int(input("Informe um numero: "))
print(a)

a += 1
print(a)

a += 1
print(a)

#Exemplo com estrutura de repetição utilizando o for:
# Receba um numero do teclado e exibe o numeor e os 2 numeros seguintes.
numero = int(input("Informe um numero: "))
for i in range(3):
    print(numero)
    numero += 1
    
    
##FOR -> é usado para percorrer uma objeto iterável (list, tuple, range, etc) ou uma sequência de valores.
#Faz sentido usar FOR quando sabemos o numero exato de vezes que o codigo sera executado.
#Exemplo:
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print()