#São operadores utilizados para verificar se um objeto está presente em uma sequência (lista, tupla, string, etc).
#Exemplo:
curso= "Curso de Python"
frutas = ["laranja", "uva" , "limão"]
saques = [1500, 100]

"Python" in curso
##Retorna True, pois a string "Python" está presente na variável curso.

"Maçã" not in frutas
##Retorna True, pois a string "Maçã" não está presente na lista frutas

2000 in saques
##Retorna False, pois o valor 2000 não está presente na lista saques

#Treinando mais:
frutas = ["limão", "uva"]
curso = "Curso de Python"

print("laranja" in frutas)
print("UVA" in frutas) ##False pois é CASE SENSITIVE!!!
print ("limão" not in frutas)
print ("Python" in curso)