while True:
    numero = int(input("informe um numero: "))
    
    if numero == 10:
        break
    
    print(numero)

#break em FOR

for numero in range(100):
    
    if numero == 15:
        break
    
    print(numero, end =" ")
    
#Usando continue -> exibir numeros impares de 0 a 100
for numero in range(100):
    
    if numero % 2 == 0:
        continue
    
    print(numero, end =" ")