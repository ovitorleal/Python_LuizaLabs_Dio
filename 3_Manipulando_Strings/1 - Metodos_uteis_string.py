# A classe String do python é famosa por ser rica em métodos e possuir
# uma interface muito facil de trabalhar.
#Ex:

curso = "pYtHon"
print (curso.upper())      # Deixa todas as letras maiúsculas
print (curso.lower())      # Deixa todas as letras minúsculas   
print (curso.title())      # Deixa a primeira letra maiúscula

#Retirando espaços em branco no início e no fim da string ou no inicio

curso = "   Python "
print (curso.strip())      # Retira os espaços em branco no início e no fim
print (curso.rstrip())     # Retira os espaços em branco no fim (direita)
print (curso.lstrip())     # Retira os espaços em branco no início(esquerda)

#Junção e Centralização de strings

curso = "Python"
print(curso.center(12, "#"))  # Centraliza a string em um campo de 10 caracteres, preenchendo com #
print(".".join(curso))        # Junta os caracteres da string com o separador "."

